from oauthlib.oauth2.rfc6749 import errors
from oauthlib.oauth2.rfc6749.grant_types.refresh_token import RefreshTokenGrant

from oauth2_provider.models import Application, AccessToken
from .backends import FirebaseAuth
from firebase_admin import auth
import logging

logger = logging.getLogger(__name__)


class FirebaseTokenGrant(RefreshTokenGrant):
    def validate_token_request(self, request):
        request._params.setdefault("client_secret", None)
        request._params.setdefault("user_id", None)

        if request.grant_type != 'convert_token':
            raise errors.UnsupportedGrantTypeError(request=request)
        # We check that a token parameter is present.
        # It should contain the social token to be used with the backend
        if request.token is None:
            raise errors.InvalidRequestError(description='Missing token parameter.', request=request)

        # We check that a user_id parameter is present.
        # It should contain the user_id that owns the token
        # Deprecated : Digits retired
        # if request.user_id is None:
        #     raise errors.InvalidRequestError(description='Missing user_id parameter.', request=request)

        if not request.client_id:
            raise errors.MissingClientIdError(request=request)

        if not self.request_validator.validate_client_id(request.client_id, request):
            raise errors.InvalidClientIdError(request=request)

        # Existing code to retrieve the application instance from the client id
        if self.request_validator.client_authentication_required(request):
            logger.debug('Authenticating client, %r.', request)
            if not self.request_validator.authenticate_client(request):
                logger.debug('Invalid client (%r), denying access.', request)
                raise errors.InvalidClientError(request=request)
        elif not self.request_validator.authenticate_client_id(request.client_id, request):
            logger.debug('Client authentication failed, %r.', request)
            raise errors.InvalidClientError(request=request)

        # Ensure client is authorized use of this grant type
        # We chose refresh_token as a grant_type
        # as we don't want to modify all the codebase.
        # It is also the most permissive and logical grant for our needs.
        request.grant_type = "refresh_token"
        self.validate_grant_type(request)

        self.validate_scopes(request)

        decoded_token = auth.verify_id_token(request.token)
        temp_id = request.temp_id if hasattr(request, 'temp_id') else None
        user = FirebaseAuth.do_auth(request, decode_token=decoded_token, temp_id=temp_id)

        if not user:
            raise errors.InvalidClientError(request=request)
        request.user = user
        logger.debug('Authorizing access to user %r.', request.user)
        # self.invalidate_existing_tokens(request.client_id, user)

    def invalidate_existing_tokens(self, client_id, user):

        """Invalidate existing tokens issued for this user."""

        app = Application.objects.get(client_id=client_id)
        tokens = AccessToken.objects.filter(user=user, application=app)
        tokens.delete()
