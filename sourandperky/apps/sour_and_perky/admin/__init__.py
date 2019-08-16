from allauth.socialaccount.admin import SocialToken
from django.contrib import admin
from rest_framework.authtoken.admin import Token

for klass in [SocialToken, Token]:
    admin.site.unregister(klass)
