from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("<h1>This page is for opensourceSW final assignment</h1>")
# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def hobby(request):
    return render(request,'hobby.html')

def profile(request):
    return render(request,'profile.html')

def favorite_song(request):
    return render(request,'favorite_song.html')
