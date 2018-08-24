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
    list_display = ['__str__', full_name, 'instrument','date', 'verdict']
    list_filter  = ['date', SectionListFilter, 'instrument',]
    search_fields = (['^first_name', '^last_name', '^instrument'])
    ordering = ['date', 'time']

    def mark_as_member(self, request, queryset):
        queryset.update(verdict='Member')
        for model in queryset:
            model.save()
        mark_as_member.short_description = "Mark selected as members"

    def mark_as_reserve(self, request, queryset):
        queryset.update(verdict='Reserve')
        for model in queryset:
            model.save()
        mark_as_reserve.short_description = "Mark selected as reserves"

    def mark_as_rejected(self, request, queryset):
        queryset.update(verdict='Rejected')
        for model in queryset:
            model.save()
        mark_as_rejected.short_description = "Mark selected as rejected"

    actions = [mark_as_member, mark_as_reserve, mark_as_rejected]


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
