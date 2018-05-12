from django.contrib import admin
from .models import Musician, Conductor, ConcertoApplicant


admin.site.register(Musician)
admin.site.register(Conductor)
admin.site.register(ConcertoApplicant)
