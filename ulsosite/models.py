from django.db import models
from django.utils import timezone
from .info import (INSTRUMENT_LIST,
                   YEAR_LIST,
                   UNI_LIST,
                   DEFAULT_VENUE)

from django.db import models


# People

class Person(models.Model):
    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.instrument)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default=None, blank=True) # optional
    email = models.EmailField(max_length=100)
    instrument = models.CharField(max_length=1, choices=INSTRUMENT_LIST)
    doubling = models.CharField(max_length=50, default=None, blank=True) # optional
    uni = models.CharField(max_length=1, choices=UNI_LIST)
    other_uni = models.CharField(max_length=50, default=None, blank=True)

    class Meta:
        abstract = True
        ordering = ['instrument']

class Musician(Person):
    # date = models.DateTimeField('date entered')
    member = models.BooleanField(default=False, help_text="Admitted to ULSO y/n")
    season = models.CharField(max_length=10, blank=True, help_text="Academic year currently or last registered e.g. 2017/18")
    year = models.CharField(max_length=1, choices=YEAR_LIST)
    experience = models.TextField(default='Briefly summarise your recent orchestral experience')
    returning_member = models.BooleanField(default=False)
    subs_paid = models.BooleanField(default=False)


class ConcertoApplicant(Person):
    # date = models.DateTimeField('date submitted')
    year = models.CharField(max_length=1, choices=YEAR_LIST)
    pieces = models.TextField()
    years_ulso_member = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    second_round = models.BooleanField(blank=True, default=False)

class ConcertoWinner(Person):
    website = models.CharField(max_length=300)
    biography = models.TextField()


class CommitteeMember(Person):
    def __str__(self):
        return '{}({} {}) - {}'.format(self.role,
                                       self.first_name,
                                       self.last_name,
                                       self.season)
    season = models.CharField(max_length=10, default='2017/18', help_text='Format yyyy/yy')
    role = models.CharField(max_length=100)
    role_description = models.CharField(max_length=1000, help_text="Description provided by personally by the committee member")

    class Meta(Person.Meta):
        ordering = []

class Conductor(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    website = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, help_text='This field is not required to facilitate quick fill-in. However, it is highly advised for you fill this in ASAP.')
    phone = models.CharField(max_length=15, blank=True) # change this
    rate_per_rehearsal = models.IntegerField(default=125, help_text="Fee charged per 3 hour rehearsal.")
    rate_concert_day = models.IntegerField(default=500, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here")
    notes = models.TextField(blank=True)

# Project/Concerts

class Concert(models.Model):
    def __str__(self):
        return '{} - {} - {}'.format(self.project_term, self.concert_date, self.conductor)
    current = models.BooleanField(default=False)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    concert_date = models.DateField('concert date')
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
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
