from django.urls import path, include
from django_urls import UrlManager
from rest_auth.registration.urls import urlpatterns as _rest_auth_registration_urls
from rest_auth.urls import urlpatterns as _rest_auth_urls
from rest_framework.routers import APIRootView

from utils.urls import url_mapping
from . import views
from .router import RooterWithUrls
from .views.authentication.urls import social_auth_urls
from .views.relations import relation_urls

router = RooterWithUrls()
router.register(r'entries', views.EntryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'titles', views.TitleViewSet)
router.register(r'title_channels', views.TitleChannelViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'user_trophies', views.UserTrophyViewSet)
router.register(r'notifications', views.NotificationViewSet)

rest_auth_registration_urls = UrlManager()
rest_auth_registration_urls.extend(_rest_auth_registration_urls)

rest_auth_urls = UrlManager()
rest_auth_urls.extend(_rest_auth_urls)


@rest_auth_registration_urls.path('', name='auth_registration')
class Registration(APIRootView):
    """Registration endpoints."""
    api_root_dict = url_mapping(rest_auth_urls.url_patterns)


rest_auth_urls.extend([path('registration/', include(rest_auth_registration_urls.url_patterns))])


@rest_auth_urls.path('', name='auth')
class Authentication(APIRootView):
    "Authentication endpoints."
    api_root_dict = url_mapping(rest_auth_urls.url_patterns)


api_urls = [
    path('social_auth/', include(social_auth_urls.url_patterns)),
    path('auth/', include(rest_auth_urls.url_patterns)),
    path('relations/', include(relation_urls.url_patterns)),
]

router.register_extra_urls(api_urls)

api_urls += [
    path('', include(router.urls))
]
