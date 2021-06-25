import firebase_admin
import json, os, pwd
from braces.views import CsrfExemptMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.settings import oauth2_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .oauth2_endpoints import FirebaseTokenServer
from .oauth2_backends import KeepRequestCore
from firebase_admin import credentials
from django.conf import settings
from oauth2_provider.models import AccessToken

# Create your views here.
def initialize_firebase_admin():
    cred = credentials.Certificate(
        f'{settings.PROJECT_DIR}/environments/market-server-firebase-adminsdk-jk5b3-25135a3a38.json'
    )
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://market-server.firebaseio.com',
                                         'storageBucket': 'market-server.appspot.com'
                                         })
    print("firebase-admin initialized...")


class ConvertTokenView(CsrfExemptMixin, OAuthLibMixin, APIView):
    server_class = FirebaseTokenServer
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = KeepRequestCore
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status = self.create_token_response(request._request)

        # data = json.loads(body)
        response = Response(data=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response


class RefreshTokenView(CsrfExemptMixin, OAuthLibMixin, APIView):
    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        request._request.POST = request._request.POST.copy()
        for key, value in request.data.items():
            request._request.POST[key] = value

        url, headers, body, status = self.create_token_response(request._request)
        if status == 200:
            access_token = json.loads(body).get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,
                    token=token)

            data = json.loads(body)
            data['is_new_user'] = False
            try:
                user = AccessToken.objects.get(token=access_token).user
                data['uid'] = user.id
                data['user_id'] = user.id
            except AccessToken.DoesNotExist:
                pass
            response = Response(data=data, status=status)
        else:
            response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v
        return response