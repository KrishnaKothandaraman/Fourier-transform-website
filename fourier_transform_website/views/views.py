from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def userDrawing(request):
    return render(request, "userDrawing.html", {})

def imageDrawing(request):
    return render(request, "imageDrawing.html", {})