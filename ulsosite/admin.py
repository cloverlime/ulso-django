from django.contrib import admin
from django.db.models import Q

from django.utils.translation import gettext_lazy as _
import nested_admin

from ulso.settings import BASE_DIR

# from ulsosite.utils import image_preview

from ulsosite.models.models_concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from ulsosite.models.models_cms import (
                        Page,
                        Section,
                        Subsection,
                        ImageSection
                        )

from ulsosite.models.models_people import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        CommitteeMember,
                        ConcertoWinner,
                        UsefulContact,
                        )

from ulsosite.models.models_auditions import (
                                            AuditionSlot,
                                            AuditionDate,
                                            )




# Admin-Wide Utils ------------------

def mark_as_member(self, request, queryset):
    queryset.update(status='Member')
    mark_subs_paid.short_description = "Mark selected as members"

def mark_as_reserve(self, request, queryset):
    queryset.update(status='Reserve')
    mark_subs_paid.short_description = "Mark selected as reserves"

def mark_as_rejected(self, request, queryset):
    queryset.update(status='Rejected')
    mark_subs_paid.short_description = "Mark selected as rejected"

def full_name(obj):
    return '{} {}'.format(obj.first_name, obj.last_name)

full_name.short_description = 'Name'

class SectionListFilter(admin.SimpleListFilter):
    title = _('section')
    parameter_name = 'instrument'

    def lookups(self, request, model_admin):
        return (
        ('Wind', 'Wind' ),
        ('Brass', 'Brass'),
        ('Strings', 'Strings'),
        ('Percussion', 'Percussion'),
        ('Other', 'Other'),
        )

    def queryset(self, request, queryset):
        if self.value() == "Wind":
            return queryset.filter(
                                    Q(instrument='Flute') |
                                    Q(instrument='Clarinet') |
                                    Q(instrument='Oboe') |
                                    Q(instrument='Bassoon')
                                    )
        if self.value() == "Brass":
            return queryset.filter(
                                    Q(instrument='Horn') |
                                    Q(instrument='Trumpet') |
                                    Q(instrument='Trombone') |
                                    Q(instrument='Tuba')
                                    )
        if self.value() == "Strings":
            return queryset.filter(
                                    Q(instrument='Violin') |
                                    Q(instrument='Viola') |
                                    Q(instrument='Cello') |
                                    Q(instrument='Bass')
                                    )
        if self.value() == "Percussion":
            return queryset.filter(instrument='Percussion')

#-------------------




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

class ImageSection(nested_admin.NestedStackedInline):
    model = ImageSection
    extra = 0

class SubsectionInline(nested_admin.NestedStackedInline):
    model = Subsection
    extra = 0

class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    extra = 1
    inlines = [SubsectionInline]

class PageAdmin(nested_admin.NestedModelAdmin):
    fields = ['page_title', 'main_description']
    inlines = [SectionInline, ImageSection]

# class SectionAdmin(admin.ModelAdmin):
#     fields = ['h2_title', 'section_description']
#     inlines = [SubsectionInline]

admin.site.register(Page, PageAdmin)


# Auditions Admin
class AuditionSlotAdmin(admin.ModelAdmin):
    list_display = ['__str__', full_name, 'instrument','date']
    list_filter  = ['date', SectionListFilter, 'instrument',]


class AuditionSlotInline(admin.TabularInline):
    model = AuditionSlot
    exclude = ['notes']
    extra = 1


class AuditionDateAdmin(admin.ModelAdmin):
    inlines = [AuditionSlotInline]
    list_display = ['day_date', 'season']
    list_filter = ['season']
    readonly_fields = ['season']


# Musicians Admin

class MusicianAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'status', 'subs_paid', 'privacy_policy', 'season')
    list_filter = ('status', SectionListFilter, 'instrument', 'subs_paid')
    readonly_fields = ('created', 'modified')

    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'status', 'subs_paid', 'season']}),
    ('Contact', {'fields': ['email', 'phone']}),
    ('Details', {'fields': ['instrument', 'doubling', 'uni', 'other_uni', 'year', 'experience',]}),
    ('Audition Info', {'fields': ['returning_member']}),
    ('Agreements', {'fields': ['depping_policy', 'privacy_policy']}),
    ('Read-only', {'fields': ['created', 'modified']})
    ]
    inlines = [AuditionSlotInline]

    def mark_subs_paid(self, request, queryset):
        queryset.update(subs_paid=True)
        mark_subs_paid.short_description = "Mark selected as subs paid"

    actions = ['mark_subs_paid',mark_as_member, mark_as_reserve, mark_as_rejected]


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email', 'season')
    exclude = ['created', 'modified']
    readonly_fields = ['display_photo']

    def display_photo(self, obj):
        from django.utils.html import mark_safe
        if obj.id:
            return mark_safe('<img src="{}{}" height="150" />'.format(BASER_DIR, obj.photo.url))
        return ''
    display_photo.allow_tags = True

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')
    fieldsets = [
    (None, {'fields': ['first_name', 'last_name', 'alias', 'email', 'phone', 'website']}),
    ('Fees', {'fields': ['rate_per_rehearsal', 'rate_concert_day', 'notes']}),
    # (None, {'fields': ['created', 'modified']})
    ]


class ConcertoApplicantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'instrument', 'piece', 'second_round')

class UsefulContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'role', 'email')
    exclude = ['modified']

#-----------------------------------
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
admin.site.register(Conductor, ConductorAdmin)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(ConcertoWinner)
admin.site.register(ConcertoApplicant, ConcertoApplicantAdmin)
admin.site.register(UsefulContact, UsefulContactAdmin)
admin.site.register(AuditionDate, AuditionDateAdmin)
admin.site.register(AuditionSlot, AuditionSlotAdmin)
