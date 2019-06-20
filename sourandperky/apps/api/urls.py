from django.urls import include, path
from django_urls import UrlManager
from rest_framework import routers

from . import views

api_urls = UrlManager('apps.api.views')

router = routers.DefaultRouter()
router.register(r'entries', views.EntryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'titles', views.TitleViewSet)
router.register(r'title_channels', views.TitleChannelViewSet)
router.register(r'events', views.EventViewSet)

api_urls._url_patterns += [
    path('', include(router.urls))
]
