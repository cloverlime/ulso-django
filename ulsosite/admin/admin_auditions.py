from django.contrib import admin

from ulsosite.models.models_auditions import (
AuditionSlot, AuditionDate

admin.site.register(AuditionSlot)
admin.site.register(AuditionDate)
