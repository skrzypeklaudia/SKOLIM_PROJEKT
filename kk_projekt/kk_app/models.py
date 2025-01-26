from django.db import models
from datetime import timedelta
from django.core.validators import RegexValidator

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, help_text="Tytuł albumu Skolima", blank=False, null= False) # to dodaje tam gdzie sie wpisuje co trzeba wpisac
    release_date = models.DateField(help_text="Data wydania albumu",  blank=False, null= False)

    def __str__(self):
        return f'{self.title} ({self.release_date.year})'
    
class Song(models.Model):
    time_format_validator = RegexValidator(
        regex=r'^[0-5][0-9]:[0-5][0-9]$', 
        message="Czas trwania musi być w formacie MM:SS")
    title = models.CharField(max_length=100, help_text="Tytuł piosenki Skolima")
    duration = models.CharField(max_length=8, help_text="Czas trwania piosenki w formacie MM:SS", validators=[time_format_validator])
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

