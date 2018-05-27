from django.contrib import admin
import nested_admin

from ulso_admin.models import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner,
                        AuditionSlot
                        )

from ulsosite.models import Concert, Piece, Rehearsal



class AuditionSlotInline(admin.StackedInline):
    model = AuditionSlot


class MusicianAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'status', 'subs_paid')

    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'status', 'subs_paid']}),
    ('Contact', {'fields': ['email', 'phone']}),
    ('Details', {'fields': ['instrument', 'doubling', 'uni', 'other_uni', 'year', 'experience',]}),
    ('Audition Info', {'fields': ['returning_member']})
    ]
    inlines = [AuditionSlotInline]


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email', 'season')


class ConductorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')




#-----------------------------------
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(ConcertoWinner)
admin.site.register(ConcertoApplicant)
