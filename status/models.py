import datetime
from django.db import models

from ulsosite.utils import academic_year_calc

# Create your models here.
class Status(models.Model):
    CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No' )
    )
    auditions_open = models.CharField(max_length=10, choices=CHOICES, help_text="Shows if ULSO is open to applications or not. Affects the display of the form on the website.")
    concerto_open = models.CharField(max_length=10, choices=CHOICES, help_text="Shows if ULSO is open to applications or not. Affects the display of the form on the website.")
    season = models.CharField(max_length=10, unique=True)

    created = models.DateTimeField(editable=False, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.season)

    def save(self, *args, **kwargs):
        ''' On save, update season and timestamps '''
        now = datetime.datetime.now()
        self.modified = now
        self.season = academic_year_calc(now)
        if not self.id or not self.created:
            self.created = now
        
        return super(Status, self).save(*args, **kwargs)