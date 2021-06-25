from django.contrib.auth.models import User
from oauth2_provider.oauth2_backends import OAuthLibCore
from oauth2_provider.models import AccessToken
from firebase_admin import auth
import json


class KeepRequestCore(OAuthLibCore):
    """
    Subclass of OAuthLibCore used only for the sake of keeping the django
    request object by placing it in the headers.
    This is a hack and we need a better solution for this.
    """

    def _extract_params(self, request):
        uri, http_method, body, headers = super(KeepRequestCore, self)._extract_params(request)
        headers["Django-request-object"] = request
        return uri, http_method, body, headers

    def create_token_response(self, request):
        print('okokokokokokk')
        """
        A wrapper method that calls create_token_response on `server_class` instance.
        :param request: The current django.http.HttpRequest object
        """
        uri, http_method, body, headers = self._extract_params(request)
        extra_credentials = self._get_extra_credentials(request)

        data = {item.split('=')[0]: item.split('=')[1]
                for item in body.split('&')
                if item.split('=')[1]}

        is_new_user = True
        if 'token' in data:
            decoded_token = auth.verify_id_token(data['token'])
            uid = decoded_token['uid']
            if User.objects.filter(username=uid).count() > 0:
                is_new_user = False

        headers, body, status = self.server.create_token_response(uri, http_method, body,
                                                                  headers, extra_credentials)

        data = json.loads(body)
        if 'access_token' in body:
            access_token = data['access_token']
            try:
                user = AccessToken.objects.get(token=access_token).user
                data['uid'] = user.id
                data['user_id'] = user.id
            except AccessToken.DoesNotExist:
                pass
        data['is_new_user'] = is_new_user

        uri = headers.get("Location", None)

        return uri, headers, data, status
