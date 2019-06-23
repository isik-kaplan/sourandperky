from django.urls import path, include
from rest_framework.routers import APIRootView
from utils.urls import url_mapping

from .google import google_urls

social_auth_urls = [
    path('google/', include((google_urls.url_patterns, 'api'), namespace='google_auth'))
]

url_mapping_for_social_auth_urls = url_mapping(social_auth_urls, 'api')

social_auth_urls.extend([
    path('', APIRootView.as_view(api_root_dict=url_mapping_for_social_auth_urls), name='social_auth')
])

