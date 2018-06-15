from django.db import models

class Page(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True)


class Section(models.Model):
    def __str__(self):
        return "{} {}".format(self.order, self.heading)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(primary_key=True)
    heading = models.CharField(max_length=100, blank=True, null=True)
    subheading = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, help_text="HTML tags required!")

class AccordionCard(models.Model):
    def __str__(self):
        return "{} {}".format(self.order, self.heading)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    order = models.PositiveIntegerField(primary_key=True, help_text="Order of display in the page.")
    body = models.TextField(blank=True, help_text="HTML tags required!")
    html_id = models.CharField(max_length=20, help_text="REQUIRED for accordions. No spaces and case-sensitive!")


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
