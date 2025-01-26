from rest_framework import serializers
from datetime import date
from .models import Album, Song, Concert, Collaboration
import re


class AlbumSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Tytuł albumu powinien zaczynać się wielką literą!")
        return value
    
    def validate_release_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Data wydania albumu nie może być w przyszłości!")
        return value

    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date']
        read_only_fields = ['id']

class SongSerializer(serializers.ModelSerializer):
    # Walidator dla title
    def validate_title(self, value):
        # Użycie capitalize() zapewni, że tylko pierwsza litera będzie wielka
        capitalized_value = value.capitalize() 
        return capitalized_value
    
    def validate_duration(self, value):
        # Sprawdzamy, czy tekst jest w formacie HH:MM:SS, gdzie HH, MM, SS to cyfry, a ":" to separator
        if not re.match(r'^\d{2}:\d{2}:\d{2}$', value):  
            raise serializers.ValidationError("Czas trwania piosenki powinien być w formacie 'HH:MM:SS' i zawierać tylko cyfry oraz dwukropek!")
        return value

    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album', 'release_date']
        read_only_fields = ['id']

    # Walidator dla release_date
    def validate_release_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Data wydania piosenki nie może być w przyszłości!")
        return value


class ConcertSerializer(serializers.ModelSerializer):
    # Walidator dla `artist`
    def validate_artist(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Nazwa artysty powinna zaczynać się wielką literą!")
        return value

    # Walidator dla location
    def validate_location(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Nazwa lokalizacji powinna zaczynać się wielką literą!")
        return value

    class Meta:
        model = Concert
        fields = ['id', 'artist', 'location', 'date']
        read_only_fields = ['id']

    # Walidator dla `date`
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Data koncertu nie może być w przeszłości!")
        return value


class CollaborationSerializer(serializers.ModelSerializer):
    # Walidator dla collaboration
    def validate_collaboration(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Nazwa kolaboracji powinna zaczynać się wielką literą!")
        return value

    # Walidator dla song_title
    def validate_song_title(self, value):
        if not value.istitle():
            raise serializers.ValidationError("Tytuł piosenki powinien zaczynać się wielką literą!")
        return value

    class Meta:
        model = Collaboration
        fields = ['id', 'collaboration', 'song_title']
        read_only_fields = ['id']
