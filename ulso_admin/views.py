from django.shortcuts import render

def index(request):
    return HttpResponse("Here is the Index of the ULSO committee dashboard")
