from django.http import HttpResponse
from django.shortcuts import render
def get_books(request):
    return HttpResponse("Welcome to the NouveauLib page.")


def greet(request, name):
    return render(request, "index.html", {'Christy': name})


# Create your views here.
