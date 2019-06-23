from django.urls import path, include

from . import views
from .router import RooterWithUrls
from .views.authentication.urls import social_auth_urls
from rest_auth.urls import urlpatterns as rest_auth_urls
from rest_framework.routers import APIRootView
from utils.urls import url_mapping
from rest_auth.registration.urls import urlpatterns as rest_auth_registration_urls

router = RooterWithUrls()
router.register(r'entries', views.EntryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'titles', views.TitleViewSet)
router.register(r'title_channels', views.TitleChannelViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'user_trophies', views.UserTrophyViewSet)
router.register(r'notifications', views.NotificationViewSet)

rest_auth_registration_urls += [
    path('', APIRootView.as_view(api_root_dict=url_mapping(rest_auth_urls)), name='auth_registration'),
]

rest_auth_urls += [
    path('registration/', include(rest_auth_registration_urls))
]

rest_auth_urls += [
    path('', APIRootView.as_view(api_root_dict=url_mapping(rest_auth_urls)), name='auth'),
]

api_urls = [
    path('social_auth/', include(social_auth_urls)),
    path('auth/', include(rest_auth_urls))
]

router.register_extra_urls(api_urls)

api_urls += [
    path('', include(router.urls))
]
