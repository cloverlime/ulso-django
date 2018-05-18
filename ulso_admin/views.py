from django.shortcuts import render
from django.http import HttpResponse
from .serializers import serialize_to_JSON
from .models import Conductor

def index(request):
    return HttpResponse("Here is the Index of the ULSO committee dashboard")

def testjson(request):
    conductors = Conductor.objects.all()
    testjson = serialize_to_JSON(conductors)
    context = {'testjson': testjson }
    return render(request, 'ulso_admin/testjson.html', context)

#
# class SerializeToJSON:
#     QUERY_SETS = (
#                 (Conductors)
#
#     )
#
#
#     def serialize_to_JSON(query_set):
#         return serializers.serialize('json', query_set)
#
#     conductors =  Conductor.objects.all()
