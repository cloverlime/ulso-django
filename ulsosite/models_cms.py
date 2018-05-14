from django.db import models

class Page(models.Model):
    def __str__(self):
        return self.h1_title
    h1_title = models.CharField(max_length=50)
    main_description = models.TextField()

class Section(models.Model):
    def __str__(self):
        return self.h2_title
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    h2_title = models.CharField(max_length=100)
    section_description = models.TextField()

class Subsection(models.Model):
    def __str__(self):
        return self.h3_title
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    h3_title = models.CharField(max_length=100)
    sub_description = models.TextField()
