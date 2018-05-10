from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Here is the Index page")

def whatson(request):
    return HttpResponse("Here is the whatson page")

def rehearsals(request):
    return HttpResponse("Here is the rehearsals page")

def contact(request):
    return HttpResponse("Here is the contact page")

def concerto(request):
    return HttpResponse("Here is the page for the concerto competition")
