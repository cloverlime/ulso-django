from django.contrib import admin
import nested_admin

from ulso_admin.models import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner,
                        )

from .models import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from .models_cms import (
                        Page,
                        Section,
                        Subsection,
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
                                    'wind',
                                    'brass',
                                    'timps',
                                    'percussionists',
                                    'percussion_equipment',
                                    'other'],
                        'classes': ['collapse']}),
                        ]
    inlines = [PiecesInline]
    exclude = ('concert',)



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]



admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Rehearsal)

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
