"""Views for the first_app application."""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    filters = {"value": "We are learning filters."}
    return render(request, "first_app/index.html", filters)


def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to the home page.</h1>")


def educative(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to the Educative page!</h1>")
