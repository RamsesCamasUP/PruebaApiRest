from .views import ListVideo, DetailVideo
from django.urls import path,re_path

urlpatterns = [
    re_path(r'^videos/$',ListVideo.as_view(),name='lista-video'),
    re_path(r'^videos/(?P<pk>[0-9]+)$',DetailVideo.as_view(),name='detail-video'),
]
