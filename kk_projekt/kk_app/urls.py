from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.album_list),
    path('albums/<int:pk>/', views.album_detail),
    path('songs/', views.song_list),
    path('songs/<int:pk>/', views.song_detail),
    path('concerts/', views.concert_list),
    path('concerts/<int:pk>/', views.concert_detail),
    path('collaborations/', views.collaboration_list),
    path('collaborations/<int:pk>/', views.collaboration_detail),
    path('songs_html/', views.song_list_html),
    path('songs_html/<int:id>/', views.song_detail_html),
    path('albums_html/', views.album_list_html),
    path('albums_html/<int:id>/', views.album_detail_html),
    path('concerts_html/', views.concert_list_html),
    path('concerts_html/<int:id>/', views.concert_detail_html),
    path('collaborations_html/', views.collaboration_list_html),
    path('collaborations_html/<int:id>/', views.collaboration_detail_html),
]
