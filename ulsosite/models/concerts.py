from django.db import models
from django.utils import timezone

from ulsosite.info.info import DEFAULT_VENUE

from .people import Conductor, Musician


class Concert(models.Model):
    def __str__(self):
        return '{} - {} - {}'.format(self.project_term, self.concert_date, self.conductor)
    current = models.BooleanField(default=False)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    concert_date = models.DateField('concert date')
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, blank=True, null=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=200, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)

    # player list
    player = models.ManyToManyField(Musician)


class Piece(models.Model):
    def __str__(self):
        return '{} - {}'.format(self.composer, self.piece)

    def __repr__(self):
        return """{} - {}, {} mins,
            Wind: {}.{}.{}.{}
            Brass: {}.{}.{}.{}
            Strings: {}.{}.{}.{}
            Timps: {}
            Perc: {}
            Harps: {}
            Notes: {}
                   {}
                   {}
                   {}
        """.format(self.composer,
                    self.piece,
                    self.flutes,
                    self.clarinets,
                    self.oboes,
                    self.bassoons,
                    self.horns,
                    self.trumpets,
                    self.trombones,
                    self.tubas,
                    self.violin_1,
                    self.violin_2,
                    self.violas,
                    self.cellos,
                    self.basses,
                    self.timps,
                    self.percussionists,
                    self.harps,
                    self.wind_notes,
                    self.brass_notes,
                    self.strings_notes,
                    self.other,
                    )

    def return_orchestration(self):
        return self.__repr__

    concert = models.ManyToManyField(Concert, blank=True)
    composer = models.CharField(max_length=20, help_text='Surname only')
    piece = models.CharField(max_length=200, help_text='Name of piece')
    order = models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')
    duration = models.IntegerField(default=0, help_text="Length in minutes",blank=True, null=True)

    # Orchestration
    flutes = models.IntegerField(blank=True, null=True)
    clarinets = models.IntegerField(blank=True, null=True)
    oboes = models.IntegerField(blank=True, null=True)
    bassoons = models.IntegerField(blank=True, null=True)
    wind_notes = models.CharField(blank=True, max_length=200, help_text='e.g. alto, picc, contra requirements')
    horns = models.IntegerField(blank=True, null=True)
    trumpets = models.IntegerField(blank=True, null=True)
    trombones = models.IntegerField(blank=True, null=True)
    tubas = models.IntegerField(blank=True, null=True)
    brass_notes = models.CharField(blank=True, max_length=200)
    violin_1 = models.IntegerField('First violins', blank=True, null=True)
    violin_2 = models.IntegerField('Second violins', blank=True, null=True)
    violas = models.IntegerField(blank=True, null=True)
    cellos = models.IntegerField(blank=True, null=True)
    basses = models.IntegerField('Double basses', blank=True, null=True)
    strings_notes = models.CharField(blank=True, max_length=200)

    harps = models.IntegerField(blank=True, help_text="Number of harps", null=True)
    timps = models.BooleanField(blank=True, default=True)
    percussionists = models.IntegerField(blank=True, default=3, help_text="Number of percussionists requried", null=True)
    other = models.TextField(blank=True, help_text="Equipment notes")


class Rehearsal(models.Model):
    """
    Each project has many rehearsals.
    Each rehearsal has one venue.
    Each rehearsal has an absence list, preferable pre-populated by forms filled
    in by players, but entries can be added manually too.

    NB. GDPR!!!!!
    """
    def __str__(self):
        return '{} {}-{}'.format(str(self.rehearsal_date), str(self.start_time), str(self.end_time))
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    rehearsal_date = models.DateField('rehearsal date')
    start_time = models.TimeField(default='19:00:00')
    end_time = models.TimeField(default='22:00:00')
    rehearsal_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    # venue = models.ManyToManyField(Venue)
    notes = models.CharField(max_length=400, blank=True)


# class PlayerPerProject(models.Model):
#     project = models.ForeignKey(Concert, on_delete=models.SET_NULL, blank=True, null=True)
#     musician = models.OneToOneField(Musician, on_delete=models.SET_NULL, blank=True, null=True)


class Absence(models.Model):
    """
    In each rehearsal, there will inevitably be some players who have to miss it.
    The orchestral manager needs to keep track of these.
    Ideally, the players would report these in advance.
    The players must already be in the list of players assigned to the concert.
    """
    rehearsal = models.ForeignKey(Rehearsal, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, help_text="First name and last name as registered")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    dep_first_name = models.CharField(max_length=20, help_text="Dep's first name")
    dep_last_name = models.CharField(max_length=20, help_text="Dep's last name")
    reasons = models.CharField(max_length=200, help_text="Reasons for absence")



# TODO - Currently not linked to anything - sort this out
class Venue(models.Model):
    # concert = models.ForeignKey(Concert, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40, help_text="Official name e.g. 'St Stephen\'s Church'")
    address_1 =  models.CharField(max_length=200, help_text="First line of address")
    address_2 =  models.CharField(max_length=200, help_text="Second line of address", blank=True, null=True)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    rate_per_rehearsal = models.IntegerField(default=90, help_text="Fee charged per 3 hour rehearsal.", blank=True, null=True)
    rate_concert_day = models.IntegerField(default=140, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here.", blank=True, null=True)
    rate_per_hour = models.IntegerField(default=90, help_text="Alternative to the above fee structures", blank=True, null=True)
