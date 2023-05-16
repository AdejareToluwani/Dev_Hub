from django.shortcuts import render, HttpResponse


# Create your views here.


def Home(requests):
    return HttpResponse('<h1> Testing Homepage </h1>')
