from django.contrib import admin
import nested_admin

from .models import (
                        Concert,
                        Piece,
                        Rehearsal,
                        CommitteeMember,
                        ConcertoWinner,
                        )

from .models_cms import (
                        Page,
                        Section,
                        Subsection,
                        )

# Register your models here.

class PiecesInline(admin.TabularInline):
    model = Piece
    extra = 1

class ConcertAdmin(admin.ModelAdmin):
    fields = ['current', 'project_term', 'start_time', 'concert_date', 'conductor', 'conductor_website', 'soloist', 'soloist_website','concert_venue']
    inlines = [PiecesInline]

admin.site.register(Concert, ConcertAdmin)
admin.site.register(Piece)
admin.site.register(Rehearsal)
admin.site.register(CommitteeMember)
admin.site.register(ConcertoWinner)


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
admin.site.register(Section)
admin.site.register(Subsection)
