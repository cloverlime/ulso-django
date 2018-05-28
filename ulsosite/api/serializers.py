from django.core import serializers
from ulsosite.models.models_people import Conductor

# Django serializers translate Django objects into standard formats like xml and json
# Django's built-in serializers are classes derived from Python's encoders
# The difference here is that e.g. JSONEncoder will turn dictionaries into JSON objects,
# DjangoJSONEncoder turns a Django model instance into a JSON object!

# High-level

# serialized_data = serializers.serialize(format, QuerySet, fields=fields)

# format = 'xml', 'json'

# # e.g. (object --> JSON)
#
# json_data = serializers.serialize('json', SomeModel.objects.all(), fields=('field1','field2')

# This stuff will work as expected, but it is quite simple. You can save the resulting serialized
# data into a files, and convert them back into 'live' objects with no loss of information.
# However, the question I want to answer is how to turn the data into an API endpoint
# so that ANY other application can take the data and convert it to whatever the application needs,
# without needing to know any implementation details of the service that OFFERS the data



def serialize_to_JSON(query_set):
    return serializers.serialize('json', query_set)
