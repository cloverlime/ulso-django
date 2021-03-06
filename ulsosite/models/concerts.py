from django.db import models
from django.utils import timezone

from ulsosite.info.info import DEFAULT_VENUE

from .people import Conductor, Musician

from ulsosite.utils import (
    academic_year_calc, format_time, format_date
)

class Concert(models.Model):
    current = models.BooleanField(default=False, help_text='Is this the current project i.e. are rehearsals imminent or underway?')
    recruiting = models.BooleanField(default=False, help_text="Do you want the project form to display this project?")
    season = models.CharField(max_length=10, null=True, blank=True)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    date = models.DateField('concert date')
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, blank=True, null=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=200, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    # player list
    players = models.ManyToManyField(Musician, related_name='players')

    def __str__(self):
        return '{} - {} - {}'.format(
            self.project_term, self.date, self.conductor)

    def save(self, *args, **kwargs):
        """Calculates season upon save"""
        if not self.season:
            self.season = academic_year_calc(self.date)
        return super(Concert, self).save(*args, **kwargs)    

class Poster(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    poster = models.ImageField(null=True, blank=True, upload_to='posters')
    artist = models.CharField(max_length=30, help_text='name of the artist')
    website = models.CharField(max_length=200, blank=True, help_text="Artist's website, if exists")


class Piece(models.Model):
    concert = models.ManyToManyField(Concert, blank=True)
    composer = models.CharField(max_length=20, help_text='Surname only')
    piece = models.CharField(max_length=200, help_text='Name of piece')
    order = models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')
    duration = models.IntegerField(default=0, help_text="Length in minutes",blank=True, null=True)
    
    def __str__(self):
        return '{} - {}'.format(self.composer, self.piece)


class Rehearsal(models.Model):
    """
    Each project has many rehearsals.
    Each rehearsal has one venue.
    Each rehearsal has an absence list, preferable pre-populated by forms filled
    in by players, but entries can be added manually too.

    """
    def __str__(self):
        return '{} {}-{}'.format(
            format_date(self.date),
            format_time(self.start_time),
            format_time(self.end_time)
        )
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    date = models.DateField('rehearsal date')
    start_time = models.TimeField(default='19:00:00')
    end_time = models.TimeField(default='22:00:00')
    rehearsal_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    notes = models.CharField(max_length=400, blank=True)


class Absence(models.Model):
    """
    In each rehearsal, there will inevitably be some players who have to miss it.
    Ideally, the players would report these in advance (e.g. via the form). 
    The players must already be in the list of players assigned to the concert.
    """
    rehearsal = models.ForeignKey(Rehearsal, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=30, help_text="As registered")
    last_name = models.CharField(max_length=30, help_text="As registered")
    email = models.EmailField("Your email address", max_length=100, help_text="As registered")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, blank=True, null=True)
    instrument = models.CharField(max_length=20)
    dep_name = models.CharField('Full name of dep', max_length=20, blank=True, null=True)
    dep_email = models.EmailField("Dep's email address", max_length=100, help_text="This is for us to notify your dep about our privacy policy, and gives them information on how to contact us if need be.", blank=True, null=True)
    dep_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Please give us your dep's phone number if at all possible. We will only contact them in the case of unexpected events to do with the rehearsal.")
    reasons = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(editable=False, blank=True, null=True)

    # TODO Fill this out more
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        ''' On receipt, create timestamps and assign to an existing Musician '''
        if not self.id or not self.timestamp:
            self.timestamp = timezone.now()
        # TODO decide if this part goes in the form or not....
        if not self.musician:
            try:
                self.musician = Musician.candidates.get(
                    first_name=self.first_name,
                    last_name=self.last_name,
                    email=self.email
                )
            except:
                return super(Absence, self).save(*args, **kwargs)
        return super(Absence, self).save(*args, **kwargs)


# TODO - Currently not linked to anything - sort this out
class Venue(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40, help_text="Official name e.g. 'St Stephen\'s Church'")
    address_1 =  models.CharField(max_length=200, help_text="First line of address")
    address_2 =  models.CharField(max_length=200, help_text="Second line of address", blank=True, null=True)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    rate_per_rehearsal = models.IntegerField(default=90, help_text="Fee charged per 3 hour rehearsal.", blank=True, null=True)
    rate_concert_day = models.IntegerField(default=140, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here.", blank=True, null=True)
    rate_per_hour = models.IntegerField(default=90, help_text="Alternative to the above fee structures", blank=True, null=True)
