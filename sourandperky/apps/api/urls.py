from django.urls import path, include

from . import views
from .router import RooterWithUrls
from .views.authentication.urls import social_auth_urls

router = RooterWithUrls()
router.register(r'entries', views.EntryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'titles', views.TitleViewSet)
router.register(r'title_channels', views.TitleChannelViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'user_trophies', views.UserTrophyViewSet)
router.register(r'notifications', views.NotificationViewSet)

api_urls = [
    path('social_auth/', include(social_auth_urls)),
]

router.register_extra_urls(api_urls)

api_urls += [
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('', include(router.urls))
]
