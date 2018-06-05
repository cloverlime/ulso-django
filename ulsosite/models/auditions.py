from django.db import models
from .people import *

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
    musician = models.OneToOneField(Musician, null=True, blank=True, on_delete=models.SET_NULL, help_text="Names and instruments will be automatically generated from this field")
    first_name = models.CharField(max_length=20, null=True, blank=True, help_text="If a Musician is not already selected, this form will attempt to find the right one by matching their name and instrument")
    last_name = models.CharField(max_length=20, null=True, blank=True)
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST, null=True, blank=True)
    verdict = models.CharField(max_length=30, choices=MEMBERSHIP_STATUS, default="Candidate")
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return (self.time).strftime('%-H:%M')

    def __repr__(self):
        return '{} - {} - {} {} ({})'.format(self.date, '__str__', self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if not self.musician:
            self.musician = Musician.candidates.get(first_name=self.first_name, last_name=self.last_name, instrument=self.instrument)
        elif self.musician and not (self.first_name or self.last_name or self.instrument):
            self.first_name = (self.musician).first_name
            self.last_name = (self.musician).last_name
            self.instrument = (self.musician).instrument
        if self.verdict != (self.musician).status:
                self.musician.status = self.verdict
                self.musician.save()
        return super(AuditionSlot, self).save(*args, **kwargs)

# Concerto Competition - could inherit instead

class ConcertoAuditionDate(models.Model):
    pass

class ConcertoAuditionRound(models.Model):
    audition_date = models.CharField(max_length=30, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    musician = models.ForeignKey('ConcertoApplicant', null=True, on_delete=models.SET_NULL)
