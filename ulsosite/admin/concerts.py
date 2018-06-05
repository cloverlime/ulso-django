from django.contrib import admin


from ulsosite.models.concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

class PiecesInline(admin.TabularInline):
    model = Piece.concert.through
    extra = 1

class RehearsalInline(admin.TabularInline):
    model = Rehearsal
    extra = 0

class ConcertAdmin(admin.ModelAdmin):
    fields = ['current', 'project_term', 'start_time', 'concert_date', 'conductor', 'soloist', 'soloist_website','concert_venue']
    inlines = [PiecesInline, RehearsalInline]

class PieceAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, { 'fields': ['composer', 'piece','order']}),
    ('Orchestration', {'fields': ['duration',
                                  ('flutes',
                                  'clarinets',
                                  'oboes',
                                  'bassoons'),
                                  'wind_notes',
                                  ('horns',
                                  'trumpets',
                                  'trombones',
                                  'tubas'),
                                  'brass_notes',
                                  ('violin_1',
                                  'violin_2',
                                  'violas',
                                  'cellos',
                                  'basses'),
                                  'strings_notes',
                                  'harps',
                                  'timps',
                                  'percussionists',
                                  'other'],
                                  }),]
    inlines = [PiecesInline]
    exclude = ('concert',)


#--------Registrations ---------
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Rehearsal)
