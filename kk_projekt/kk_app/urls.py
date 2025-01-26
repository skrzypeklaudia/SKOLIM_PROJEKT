from django.urls import path
from . import views
from .views import AlbumList, AlbumDetail

urlpatterns = [
    path('albums/', AlbumList.as_view(), name='album_list'),
    path('albums/<int:pk>/', AlbumDetail.as_view(), name='album_detail'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    path('concerts/', views.concert_list, name='concert_list'),
    path('concerts/<int:pk>/', views.concert_detail, name='concert_detail'),
    path('collaborations/', views.collaboration_list, name='collaboration_list'),
    path('collaborations/<int:pk>/', views.collaboration_detail, name='collaboration_detail'),
]
