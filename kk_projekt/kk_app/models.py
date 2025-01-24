from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, help_text="Tytuł albumu Skolima", blank=False, null= False) # to dodaje tam gdzie sie wpisuje co trzeba wpisac
    release_date = models.DateField(help_text="Data wydania albumu", editable="False")

    def __str__(self):
        return f"Album: {self.title} ({self.release_date.year})"
    
    
class Song(models.Model):
    title = models.CharField(max_length=100, help_text="Tytuł piosenki Skolima", blank=False, null= False)
    duration = models.DurationField(help_text="Czas trwania piosenki (HH:MM:SS)", blank=False, null=False)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE, blank= False)
    release_date = models.DateField(help_text="Data wydania piosenki")
    
    def __str__(self):
        return f' {self.title} ({self.album.title})'

class Concert(models.Model):
    artist = models.CharField(max_length=100, default="Skolim", help_text="Artysta występujący")  # Domyślnie Skolim
    location = models.CharField(max_length=200, help_text="Miejsce koncertu", blank=False, null= False)
    date = models.DateField(help_text="Data koncertu")  # Data koncertu

    def __str__(self):
        return f"{self.artist} - {self.location} ({self.date})"
    
class Collaboration(models.Model):
    collaboration = models.CharField(max_length=100)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.collaboration

