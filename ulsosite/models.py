from django.db import models
from django.utils import timezone
from django.db import models

from .info import (INSTRUMENT_LIST,
                   YEAR_LIST,
                   UNI_LIST,
                   DEFAULT_VENUE)

from ulso_admin.models import Conductor


# Project/Concerts

class Concert(models.Model):
    def __str__(self):
        return '{} - {} - {}'.format(self.project_term, self.concert_date, self.conductor)
    current = models.BooleanField(default=False)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    concert_date = models.DateField('concert date')
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, blank=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=200, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)


class Piece(models.Model):
    def __str__(self):
        return '{} - {}'.format(self.composer, self.piece)
    concert = models.ManyToManyField(Concert, blank=True)
    composer = models.CharField(max_length=20, help_text='Surname only')
    piece = models.CharField(max_length=200)
    order = models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')
    notes = models.CharField(max_length=200, blank=True, help_text='Give any particular details e.g. "needs 3 contrabassoons"')

class Rehearsal(models.Model):
    def __str__(self):
        return '{} {}-{}'.format(str(self.rehearsal_date), str(self.start_time), str(self.end_time))
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    rehearsal_date = models.DateField('rehearsal date')
    start_time = models.TimeField(default='19:00:00')
    end_time = models.TimeField(default='22:00:00')
    rehearsal_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    notes = models.CharField(max_length=400, blank=True)

# Managers and QuerySets

# class MemberQuerySet(models.QuerySet):
#     def members(self):
#         return self.filter(member=True)
#
# class InstrumentQuerySet(models.QuerySet):
#     def instrument(self, instrument):
#         return self.filter(instrument=instrument)
#
# class MusicnaManager(models.Manager)
#
