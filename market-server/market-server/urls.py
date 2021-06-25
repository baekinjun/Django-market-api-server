"""market-server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from docs.views import schema_view
from firebase_phone_oauth2.views import initialize_firebase_admin
import api.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls.urlpatterns)),
]


if settings.DEBUG:
    urlpatterns = [
        path('api/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('api/swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ] + urlpatterns

initialize_firebase_admin()
