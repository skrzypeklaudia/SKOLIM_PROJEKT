from django.contrib import admin

# Register your models here.
from .models import Album, Song, Concert, Collaboration

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Concert)
admin.site.register(Collaboration)