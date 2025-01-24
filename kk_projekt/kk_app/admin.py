from django.contrib import admin

# Register your models here.
from .models import Album, Song, Concert, Collaboration

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Concert)
class CollaborationAdmin(admin.ModelAdmin):
    # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
    list_display = ['collaboration', 'song']

# ten obiekt też trzeba zarejestrować w module admin
admin.site.register(Collaboration, CollaborationAdmin)