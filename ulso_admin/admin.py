from django.contrib import admin
import nested_admin

from ulso_admin.models import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner
                        )

from ulsosite.models import Concert, Piece, Rehearsal

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'status', 'subs_paid')

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email', 'season')

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')

admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(ConcertoWinner)
admin.site.register(ConcertoApplicant)
