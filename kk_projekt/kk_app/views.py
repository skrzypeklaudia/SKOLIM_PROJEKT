
# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Album, Song, Concert, Collaboration
from .serializers import AlbumSerializer, SongSerializer, ConcertSerializer, CollaborationSerializer


@api_view(['GET'])
def album_list(request): # wszystkie obiekty
    """
    Lista wszystkich obiektów modelu Album.
    """
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk): # operacja na pojedynczym obiekcie
    """
    Szczegóły pojedynczego obiektu Album.
    """
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def song_list(request):
    """
    Lista wszystkich obiektów modelu Song oraz dodawanie nowych.
    """
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    """
    Wyświetlanie, edytowanie i usuwanie pojedynczego obiektu modelu Song.
    """
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def concert_list(request):
    """
    Lista wszystkich obiektów modelu Concert.
    """
    if request.method == 'GET':
        concerts = Concert.objects.all()
        serializer = ConcertSerializer(concerts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def concert_detail(request, pk):
    """
    Szczegóły pojedynczego obiektu Concert.
    """
    try:
        concert = Concert.objects.get(pk=pk)
    except Concert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConcertSerializer(concert)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConcertSerializer(concert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        concert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def collaboration_list(request):
    """
    Lista wszystkich obiektów modelu Collaboration.
    """
    if request.method == 'GET':
        collaborations = Collaboration.objects.all()
        serializer = CollaborationSerializer(collaborations, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def collaboration_detail(request, pk):
    """
    Szczegóły pojedynczego obiektu Collaboration.
    """
    try:
        collaboration = Collaboration.objects.get(pk=pk)
    except Collaboration.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollaborationSerializer(collaboration)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollaborationSerializer(collaboration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        collaboration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home_view_html(request):
    return render(request, 'kk_app/home.html')

def albums_view_html(request):
    albums = Album.objects.all()
    return render(request, 'kk_app/albums.html', {'albums': albums})

def songs_view_html(request):
    songs = Song.objects.all()
    return render(request, 'kk_app/songs.html', {'songs': songs})

def concerts_view_html(request):
    concerts = Concert.objects.all()
    return render(request, 'kk_app/concerts.html', {'concerts': concerts})

def collaborations_view_html(request):
    collaborations = Collaboration.objects.all()
    return render(request, 'kk_app/collaborations.html', {'collaborations': collaborations})

def album_detail_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = Song.objects.filter(album=album)
    return render(request, 'kk_app/album_detail.html', {'album': album, 'songs': songs})