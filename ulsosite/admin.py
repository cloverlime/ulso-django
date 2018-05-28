from django.contrib import admin
import nested_admin

from ulsosite.models.models_concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from ulsosite.models.models_cms import (
                        Page,
                        Section,
                        Subsection,
                        )

from ulsosite.models.models_people import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner,
                        AuditionSlot
                        )


# Concerts etc

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



admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Rehearsal)



# CMS Admin

class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    extra = 0

class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    extra = 1
    inlines = [SubsectionInline]

class PageAdmin(nested_admin.NestedModelAdmin):
    fields = ['h1_title', 'main_description']
    inlines = [SectionInline]

# class SectionAdmin(admin.ModelAdmin):
#     fields = ['h2_title', 'section_description']
#     inlines = [SubsectionInline]

admin.site.register(Page, PageAdmin)
# admin.site.register(Section)
# admin.site.register(Subsection)




# Auditions Admin



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
    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'alias', 'email', 'phone', 'website']}),
    ('Fees', {'fields': ['rate_per_rehearsal', 'rate_concert_day', 'notes']})
    ]


#-----------------------------------
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(ConcertoWinner)
admin.site.register(ConcertoApplicant)
