from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

from apps.api.urls import api_urls


@api_urls.re_path('^auth/google/', name='google_api_login')
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
