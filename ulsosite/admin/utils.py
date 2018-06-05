from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

# Admin-Wide Utils ------------------

# TODO Sort these out - should the description be indented?
def mark_as_member(self, request, queryset):
    queryset.update(status='Member')
    mark_as_member.short_description = "Mark selected as members"

def mark_as_reserve(self, request, queryset):
    queryset.update(status='Reserve')
    mark_as_reserve.short_description = "Mark selected as reserves"

def mark_as_rejected(self, request, queryset):
    queryset.update(status='Rejected')
    mark_as_rejected.short_description = "Mark selected as rejected"

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
