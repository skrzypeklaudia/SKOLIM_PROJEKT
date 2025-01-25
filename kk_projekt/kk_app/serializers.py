from rest_framework import serializers
from .models import Album, Song, Concert, Collaboration


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'release_date']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance


class SongSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())  # Klucz obcy do albumu

    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'album', 'release_date']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.album = validated_data.get('album', instance.album)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
    
class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ['id', 'artist', 'location', 'date']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Concert.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.artist = validated_data.get('artist', instance.artist)
        instance.location = validated_data.get('location', instance.location)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
    
class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = ['id', 'collaboration', 'song_title']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Collaboration.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.collaboration = validated_data.get('collaboration', instance.collaboration)
        instance.song_title = validated_data.get('song_title', instance.song_title)
        instance.save()
        return instance