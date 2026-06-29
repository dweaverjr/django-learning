from django.urls import path

from zing_it import views

app_name = "zing_it"

urlpatterns = [
    path("", views.home, name="home"),
    path("playlist/<int:playlist_id>/", views.playlist, name="playlist"),
    # path("about/", views.about, name="about"),
    # path("index/", views.index, name="index"),
]
