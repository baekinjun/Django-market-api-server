from django.conf.urls import url
from django.urls import path
from oauth2_provider.views import AuthorizationView, TokenView, RevokeTokenView
from .views import ConvertTokenView, RefreshTokenView

urlpatterns = [
    path('authorize/', AuthorizationView.as_view(), name="authorize"),
    path('token/', RefreshTokenView.as_view(), name="token"),
    path('convert_token/', ConvertTokenView.as_view(), name='convert_token'),
    path('revoke_token/', RevokeTokenView.as_view(), name="revoke_token"),
]