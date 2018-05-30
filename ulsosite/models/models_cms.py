from django.db import models

class Page(models.Model):
    def __str__(self):
        return self.page_title
    page_title = models.CharField(max_length=50)
    main_description = models.TextField(blank=True)

class Section(models.Model):
    def __str__(self):
        return self.h2_title
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    h2_title = models.CharField(max_length=100)
    section_description = models.TextField(blank=True)


class ImageSection(models.Model):
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField()
    alt = models.CharField(max_length=200, blank=True, null=True, help_text='Text to show on hover and if image fails')
    caption = models.CharField(max_length=400, blank=True, null=True, help_text='Public description/figcaption to go below image. Optional!')


class Subsection(models.Model):
    def __str__(self):
        return self.h3_title
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    h3_title = models.CharField(max_length=100)
    sub_description = models.TextField()
