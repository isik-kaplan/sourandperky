from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.urls import path
from django_urls import UrlManager
from rest_auth.registration.views import (
    SocialLoginView,
    SocialConnectView,
    SocialAccountDisconnectView,
)
from rest_framework.routers import APIRootView

from utils.urls import url_mapping

google_urls = UrlManager()


@google_urls.path('login/', name='google_login')
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


@google_urls.path('connect/', name='google_connect')
class GoogleConnect(SocialConnectView):
    ...


@google_urls.path('disconnect/', name='google_disconnect')
class GoogleDisconnect(SocialAccountDisconnectView):
    ...


url_mapping_for_google_urls = url_mapping(google_urls.url_patterns, 'api')

google_urls.extend([
    path('', APIRootView.as_view(api_root_dict=url_mapping_for_google_urls), name='google')
])
