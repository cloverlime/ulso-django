from django.db import models
from .models_people import *

# Main Auditions
class AuditionDate(models.Model):
    day_date = models.DateField()
    panel1 = models.CharField('panel member and instrument', max_length=40, help_text="e.g. Nathan Halsing (Flute)")
    panel2 = models.CharField('panel member and instrument', max_length=40,blank=True, null=True)
    panel3 = models.CharField('panel member and instrument', max_length=40, blank=True, null=True)
    panel4 = models.CharField('panel member and instrument', max_length=40, blank=True, null=True)
    location = models.CharField(max_length=300, default="Strand Campus, King's College London, Strand, WC2R 2LS")
    season = models.CharField(max_length=10, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['day_date']

    # TODO Not sure why day of the week isn't showing up!
    def __str__(self):
        return (self.day_date).strftime("%a %d %b %y")

    def save(self, *args, **kwargs):
        ''' On creation, assign the academic year '''
        if not self.season:
            self.season = academic_year_calc(self.day_date)
        return super(AuditionDate, self).save(*args, **kwargs)

class AuditionSlot(models.Model):
    date = models.ForeignKey(AuditionDate, on_delete=models.SET_NULL, blank=True, null=True)
    time = models.TimeField('Start time', null=True)
    musician = models.OneToOneField(Musician, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST, null=True, blank=True)

    def __str__(self):
        return (self.time).strftime('%-H:%M')

    def __repr__(self):
        return '{} - {} - {} {} ({})'.format(self.date, '__str__', self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.musician:
            self.musician = Musician.candidates.get(first_name=self.first_name, last_name=self.last_name, instrument=self.instrument)
        return super(AuditionSlot, self).save(*args, **kwargs)



# Concerto Competition - could inherit instead
class ConcertoAuditionRound(models.Model):
    audition_date = models.CharField(max_length=30, choices=CONCERTO_DATES_2017, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    musician = models.ForeignKey('ConcertoApplicant', null=True, on_delete=models.SET_NULL)
