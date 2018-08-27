from django.contrib import admin

from ulsosite.models.concerts import (
    Concert,
    Piece,
    Poster,
    Rehearsal,
    Absence
)

from ulsosite.utils import full_name

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
    list_display = ('__str__', 'current', 'recruiting')
    list_filter = ('season', 'conductor')
    fields = ['current', 'recruiting', 'project_term', 'season', 'start_time', 'date',
    'conductor', 'soloist', 'soloist_website','concert_venue']
    inlines = [PiecesInline, RehearsalInline, PosterInline, PlayersInline]
  
    def mark_as_current(self, request, queryset):
        queryset.update(current=True)
        for model in queryset:
            model.save()
        mark_as_current.short_description = "Mark selected as current"

    def mark_as_not_current(self, request, queryset):
        queryset.update(current=False)
        for model in queryset:
            model.save()
        mark_as_not_current.short_description = "Mark selected as not current"

    def mark_as_recruiting(self, request, queryset):
        queryset.update(recruiting=True)
        for model in queryset:
            model.save()
        mark_as_recruiting.short_description = "Mark selected as recruiting"

    def mark_as_not_recruiting(self, request, queryset):
        queryset.update(recruiting=False)
        for model in queryset:
            model.save()
        mark_as_not_recruiting.short_description = "Mark selected as not recruiting"

    actions = ['mark_as_current', 'mark_as_recruiting', 'mark_as_not_current', 'mark_as_not_recruiting']


class PieceAdmin(admin.ModelAdmin):
    list_display = ('composer', 'piece')
    list_filter = ('composer',)
    fields = ['composer', 'piece', 'duration', 'order']
    inlines = [PiecesInline]
    exclude = ('concert',)



class AbsenceInline(admin.TabularInline):
    model = Absence
    extra = 0


class RehearsalAdmin(admin.ModelAdmin):
    list_filter = ('concert',)
    list_display = ('concert', 'date', 'start_time', 'end_time', 'rehearsal_venue')
    inlines = [AbsenceInline]

class AbsenceAdmin(admin.ModelAdmin):
    list_display = (
        'rehearsal', full_name, 'instrument',
        'dep_name', 'dep_email', 'dep_phone'
    )
    list_filter = ('rehearsal',)


#--------Registrations ---------
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Rehearsal, RehearsalAdmin)
admin.site.register(Absence, AbsenceAdmin)
