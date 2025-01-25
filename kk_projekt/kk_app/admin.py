from django.contrib import admin

# Register your models here.
from .models import Album, Song, Concert, Collaboration
from django import forms

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_year']

    def release_year(self, obj):
        return obj.release_date.year  # Zwróci rok wydania albumu
    release_year.admin_order_field = 'release_date'  # Można sortować po dacie
    release_year.short_description = 'Rok wydania'  # Zmienia nazwę kolumny w panelu admina
admin.site.register(Album, AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'duration','release_date']

    def release_year(self, obj):
        return obj.release_date.year  # Zwróci rok wydania albumu
    release_year.admin_order_field = 'release_date'  # Można sortować po dacie
    release_year.short_description = 'Rok wydania'  # Zmienia nazwę kolumny w panelu admina
admin.site.register(Song, SongAdmin)

class ConcertAdmin(admin.ModelAdmin):
    list_display = ['artist', 'location', 'date']

    def release_year(self, obj):
        return obj.release_date.year  # Zwróci rok wydania albumu
admin.site.register(Concert, ConcertAdmin)
class CollaborationAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ['collaboration', 'song_title']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Collaboration, CollaborationAdmin)