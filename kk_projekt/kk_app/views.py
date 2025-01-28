
# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Album, Song, Concert, Collaboration
from .serializers import AlbumSerializer, SongSerializer, ConcertSerializer, CollaborationSerializer, UserSerializer


@api_view(['POST'])
def register_user(request):
    """Rejestracja nowego użytkownika."""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Użytkownik zarejestrowany pomyślnie!"}, status=status.HTTP_201_CREATED)
    return Response(request, 'kk_app/register_user.html', serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    """Logowanie użytkownika."""
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Zalogowano pomyślnie!"}, status=status.HTTP_200_OK)
    return Response(request, 'kk_app/login_user.html',{"error": "Nieprawidłowa nazwa użytkownika lub hasło."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def logout_user(request):
    """Wylogowanie użytkownika."""
    logout(request)
    return render(request, 'kk_app/logout_user.html','/')

@login_required
def user_panel(request):
    """Panel użytkownika."""
    return render(request, 'kk_app/user_panel.html', {'user': request.user})

def homepage(request):
    """Strona główna z panelem logowania."""
    if request.user.is_authenticated:
        return redirect('user_panel')  # Przekierowanie do panelu użytkownika, jeśli zalogowany
    return render(request, 'kk_app/login_panel.html')

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
    """Strona główna z panelem logowania."""
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_panel')  # Przekierowanie po zalogowaniu
        else:
            error_message = 'Nieprawidłowa nazwa użytkownika lub hasło.'

    return render(request, 'kk_app/home.html', {'error_message': error_message})

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