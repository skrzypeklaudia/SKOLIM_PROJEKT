from django.db import models
from datetime import timedelta

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, help_text="Tytuł albumu Skolima", blank=False, null= False) # to dodaje tam gdzie sie wpisuje co trzeba wpisac
    release_date = models.DateField(help_text="Data wydania albumu",  blank=False, null= False)

    def __str__(self):
        return f'{self.title} ({self.release_date.year})'
    
class Song(models.Model):
    title = models.CharField(max_length=100, help_text="Tytuł piosenki Skolima")
    duration = models.CharField(max_length=8, help_text="Czas trwania piosenki w formacie HH:MM:SS")
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    release_date = models.DateField(help_text="Data wydania piosenki")
    
    def __str__(self):
        return f"Piosenka: {self.title} (Z albumu: {self.album.title})"

class Concert(models.Model):
    artist = models.CharField(max_length=100, default="Skolim", help_text="Artysta występujący")  # Domyślnie Skolim
    location = models.CharField(max_length=200, help_text="Miejsce koncertu", blank=False, null= False)
    date = models.DateField(help_text="Data koncertu")  # Data koncertu

    def __str__(self):
        return f"{self.artist} - {self.location} ({self.date})"
    
class Collaboration(models.Model):
    collaboration = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100, help_text="Tytuł piosenki Skolima", blank=False, null=False, default="")

    def __str__(self):
        return f'{self.collaboration} {self.song_title}'

class User(models.Model):
    imie = models.CharField(max_length=100, blank=False, null=False)
    nazwisko = models.CharField(max_length=500, blank=False, null=False)
    pseudonim = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)

