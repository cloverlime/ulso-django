from django.contrib import admin
from .models import (
                        Concert,
                        Piece,
                        Rehearsal,
                        CommitteeMember,
                        ConcertoWinner,
                        )

# Register your models here.

class PiecesInline(admin.TabularInline):
    model = Piece
    extra = 1

class ConcertAdmin(admin.ModelAdmin):
    fields = ['season', 'concert_date', 'conductor', 'conductor_website', 'soloist', 'soloist_website','concert_venue']
    inlines = [PiecesInline]

admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece)
admin.site.register(Rehearsal)
admin.site.register(CommitteeMember)
admin.site.register(ConcertoWinner)
