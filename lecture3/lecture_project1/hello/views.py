from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, Bernardo")

def patricia(request):
    return HttpResponse("Hello, Patricia!")

def guy(request):
    return HttpResponse("Hello, guy!")

# an interactive function:
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

# templates:
def index(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })