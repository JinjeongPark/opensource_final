from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("<h1>This page is for opensourceSW final assignment</h1>")
# Create your views here.

def index(request):
    return render(request,'index2.html')
