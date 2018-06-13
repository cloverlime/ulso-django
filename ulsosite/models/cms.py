from django.db import models

# TODO Fix all broken things.......

class Page(models.Model):
    def __str__(self):
        return self.page_title
    page_title = models.CharField(max_length=50)
    main_description = models.TextField(blank=True)


class Section(models.Model):
    def __str__(self):
        return self.h2_title
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)

#
# class Subsection(models.Model):
#     def __str__(self):
#         return self.h3_title
#     section = models.ForeignKey(Section, on_delete=models.CASCADE)
#     h3_title = models.CharField(max_length=100)
#     sub_description = models.TextField()
#
#
# class ImageSection(models.Model):
#     page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)
#     image = models.ImageField()
#     alt = models.CharField(max_length=200, blank=True, null=True, help_text='Text to show on hover and if image fails')
#     caption = models.CharField(max_length=400, blank=True, null=True, help_text='Public description/figcaption to go below image. Optional!')
