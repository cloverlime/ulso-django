from django.contrib import admin

from .utils import (
    SectionListFilter,
    mark_as_member,
    mark_as_rejected,
    mark_as_reserve
)

from ulsosite.utils import full_name

from ulsosite.models.auditions import (
    AuditionSlot,
    AuditionDate,
)

class AuditionSlotAdmin(admin.ModelAdmin):
    list_display = ['__str__', full_name, 'instrument','date']
    list_filter  = ['date', SectionListFilter, 'instrument',]
    search_fields = (['^first_name', '^last_name', '^instrument'])
    ordering = ['date', 'time']


class AuditionSlotInline(admin.TabularInline):
    model = AuditionSlot
    exclude = ['notes']
    extra = 1


class AuditionDateAdmin(admin.ModelAdmin):
    inlines = [AuditionSlotInline]
    list_display = ['date', 'season']
    list_filter = ['season']
    readonly_fields = ['season']

#--------Registrations ---------
admin.site.register(AuditionSlot, AuditionSlotAdmin)
admin.site.register(AuditionDate, AuditionDateAdmin)
