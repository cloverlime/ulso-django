from django.contrib import admin
import nested_admin

from ulso_admin.models import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        )

from ulsosite.models import Concert, Piece, Rehearsal

admin.site.register(CommitteeMember)
admin.site.register(Conductor)
admin.site.register(Musician)
admin.site.register(ConcertoApplicant)
