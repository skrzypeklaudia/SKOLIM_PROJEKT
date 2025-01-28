from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [ 
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/<int:album_id>/', views.album_detail_view, name='album_detail'),
    path('songs/', views.song_list, name='song_list'),
    path('songs/<int:pk>/', views.song_detail, name='song_detail'),
    path('concerts/', views.concert_list, name='concert_list'),
    path('concerts/<int:pk>/', views.concert_detail, name='concert_detail'),
    path('collaborations/', views.collaboration_list, name='collaboration_list'),
    path('collaborations/<int:pk>/', views.collaboration_detail, name='collaboration_detail'),  
    path('albums_html/', views.albums_view_html, name='albums'),
    path('songs_html/', views.songs_view_html, name='songs'),
    path('concerts_html/', views.concerts_view_html, name='concerts'),
    path('collaborations_html/', views.collaborations_view_html, name='collaborations'),
    path('home_html/', views.home_view_html, name='homepage'),  # Strona główna
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('user_panel/', views.user_panel, name='user_panel'),
]
