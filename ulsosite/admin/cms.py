from django.contrib import admin
# import nested_admin

from ulsosite.models.cms import (
                        Page,
                        Section,
                        AccordionCard
                        # Subsection,
                        # ImageSection
                        )


# class ImageSection(nested_admin.NestedStackedInline):
#     model = ImageSection
#     extra = 0
#
# class SubsectionInline(nested_admin.NestedStackedInline):
#     model = Subsection
#     extra = 0

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    # inlines = [SubsectionInline]

class AccordionCardInline(admin.TabularInline):
    model = AccordionCard
    extra = 0

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'body']
    inlines = [SectionInline, AccordionCardInline]

# class SectionAdmin(admin.ModelAdmin):
#     # fields = ['h2_title', 'section_description']
#     # inlines = [SubsectionInline]

admin.site.register(Page, PageAdmin)
