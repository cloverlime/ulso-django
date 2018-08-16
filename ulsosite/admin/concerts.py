from django.contrib import admin

from ulsosite.models.concerts import (
    Concert,
    Piece,
    Poster,
    Rehearsal,
    Absence
)

from ulsosite.models.people import Musician

class PiecesInline(admin.TabularInline):
    model = Piece.concert.through
    extra = 1

class RehearsalInline(admin.TabularInline):
    model = Rehearsal
    extra = 0

class PosterInline(admin.StackedInline):
    model = Poster
    extra = 0

class PlayersInline(admin.TabularInline):
    model = Concert.players.through
    extra = 0   


class ConcertAdmin(admin.ModelAdmin):
    fields = ['current', 'project_term', 'start_time', 'date',
    'conductor', 'soloist', 'soloist_website','concert_venue']
    inlines = [PiecesInline, RehearsalInline, PosterInline, PlayersInline]



class PieceAdmin(admin.ModelAdmin):
    fields = ['composer', 'piece', 'duration', 'order']
    inlines = [PiecesInline]
    exclude = ('concert',)


class AbsenceInline(admin.TabularInline):
    model = Absence
    extra = 0


class RehearsalAdmin(admin.ModelAdmin):
    inlines = [AbsenceInline]

class AbsenceAdmin(admin.ModelAdmin):
    list_display = (
        'rehearsal', 'full_name', 'instrument',
        'dep_name', 'dep_email', 'dep_phone'
    )
    list_filter = ('rehearsal',)


#--------Registrations ---------
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Rehearsal, RehearsalAdmin)
admin.site.register(Absence, AbsenceAdmin)
