from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


my_playlists = [
    {"id": 1, "name": "Car Playlist", "numberOfSongs": 4},
    {"id": 2, "name": "Coding Playlist", "numberOfSongs": 2},
]


my_songs = [
    {
        "id": 1,
        "Track": "thank u, next",
        "Artist": "Ariana Grande",
        "Album": "thank u, next",
        "Length": "3:27",
        "playlist_id": 1,
    },
    {
        "id": 2,
        "Track": "One Kiss, next",
        "Artist": "Dua Lipa, Calvin Harris",
        "Album": "One Kiss",
        "Length": "3:34",
        "playlist_id": 1,
    },
    {
        "id": 3,
        "Track": "Better Now",
        "Artist": "Post Malone",
        "Album": "beerbongs & bentleys",
        "Length": "3:51",
        "playlist_id": 1,
    },
    {
        "id": 4,
        "Track": "The Middle",
        "Artist": "Grey,Marren Morris, ZEDD",
        "Album": "The Middle",
        "Length": "3:04",
        "playlist_id": 1,
    },
    {
        "id": 5,
        "Track": "Love Lies",
        "Artist": "Normani, Khalid",
        "Album": "Love Lies",
        "Length": "3:21",
        "playlist_id": 2,
    },
    {
        "id": 6,
        "Track": "Rise",
        "Artist": "Jack & Jack, Jonas Blue",
        "Album": "Blue",
        "Length": "3:14",
        "playlist_id": 2,
    },
]


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "zing_it/home.html",
        {"playlists": my_playlists, "songs": my_songs},
    )


def playlist(request: HttpRequest, playlist_id: int) -> HttpResponse:
    playlist = next((p for p in my_playlists if p["id"] == playlist_id), None)
    if not playlist:
        return HttpResponse("Playlist not found", status=404)

    songs = [s for s in my_songs if s["playlist_id"] == playlist_id]

    return render(
        request,
        "zing_it/songs.html",
        {"playlist": playlist, "songs": songs},
    )
