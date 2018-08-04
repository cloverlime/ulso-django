from django.contrib import admin

from ulso.settings import BASE_DIR

from ulsosite.models.people import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner,
                        UsefulContact,
                        )

from .utils import (SectionListFilter,
                    full_name,
                    mark_as_member,
                    mark_as_rejected,
                    mark_as_reserve
                    )

from .auditions import AuditionSlotInline

# Musicians Admin

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'status', 'subs_paid', 'privacy_policy', 'season')
    list_filter = ('status', SectionListFilter, 'instrument', 'subs_paid')
    readonly_fields = ('created', 'modified')
    search_fields = (['^first_name', '^last_name', '^instrument', '^university'])

    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'status', 'subs_paid', 'season']}),
    ('Contact', {'fields': ['email', 'phone']}),
    ('Details', {'fields': ['instrument', 'doubling', 'uni', 'other_uni', 'year', 'experience',]}),
    ('Audition Info', {'fields': ['returning_member']}),
    ('Agreements', {'fields': ['depping_policy', 'privacy_policy']}),
    ('Read-only', {'fields': ['created', 'modified']})
    ]
    inlines = [AuditionSlotInline]

    def mark_subs_paid(self, request, queryset):
        queryset.update(subs_paid=True)

    mark_subs_paid.short_description = "Mark selected as subs paid"

    actions = ['mark_subs_paid',mark_as_member, mark_as_reserve, mark_as_rejected]


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email', 'season')
    list_filter = ('season', 'role')
    exclude = ['created', 'modified']
    readonly_fields = ['display_photo']
    search_fields = (['^first_name', '^last_name', '^role'])

    # # TODO Sort photo display in admin
    def display_photo(self, obj):
        from django.utils.html import mark_safe
        if obj.id:
            return mark_safe('<img src="{}{}" height="150" />'.format(BASE_DIR, obj.photo.url))
        return ''
    display_photo.allow_tags = True

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')
    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'alias', 'email', 'phone', 'website']}),
    ('Fees', {'fields': ['rate_per_rehearsal', 'rate_concert_day', 'notes']}),
    # (None, {'fields': ['created', 'modified']})
    ]


class ConcertoApplicantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'piece', 'second_round')

class UsefulContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email')
    exclude = ['modified']


#--------Registrations ---------
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(ConcertoWinner)
admin.site.register(ConcertoApplicant, ConcertoApplicantAdmin)
admin.site.register(UsefulContact, UsefulContactAdmin)
