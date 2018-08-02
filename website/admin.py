from django.contrib import admin

from website.models import (
                        Page,
                        Section,
                        AccordionCard,
                        Image
                        )

# class ImageSection(nested_admin.NestedStackedInline):
#     model = ImageSection
#     extra = 0
#
# class SubsectionInline(nested_admin.NestedStackedInline):
#     model = Subsection
#     extra = 0

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    inlines = [ImageInline]

class AccordionCardInline(admin.TabularInline):
    model = AccordionCard
    extra = 0
    inlines = [ImageInline]

class PageAdmin(admin.ModelAdmin):
    fields = ['title', 'body']
    inlines = [SectionInline, AccordionCardInline]

class SectionAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

class AccordionCardAdmin(admin.ModelAdmin):
    list_display = ('page', 'order', 'heading')
    list_filter = ('page',)
    inlines = [ImageInline]

# class ImageAdmin(admin.ModelAdmin)

admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(AccordionCard, AccordionCardAdmin)
