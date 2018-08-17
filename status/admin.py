from django.contrib import admin
from .models import Status
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ('season', 'auditions_open', 'concerto_open')

admin.site.register(Status, StatusAdmin)