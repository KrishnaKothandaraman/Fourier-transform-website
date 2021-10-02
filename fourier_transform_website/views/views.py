from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html", {})

def userDrawing(request):
    return render(request, "userDrawing.html", {})

def imageDrawing(request):
    return render(request, "imageDrawing.html", {})

def process_image(request):
    print(request.POST["user_image"])

    print(request)
    
    return HttpResponse("ok")