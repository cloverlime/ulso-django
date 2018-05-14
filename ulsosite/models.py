from django.db import models
from django.utils import timezone

# Useful data
DEFAULT_VENUE = "St. Stephen's Church, Gloucester Road, SW7 4RL"

class Concert(models.Model):
    def __str__(self):
        return self.project_term + ' ' + str(self.concert_date)
    current = models.BooleanField(default=False)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    concert_date = models.DateField('concert date')
    conductor = models.CharField(max_length=100)
    conductor_website = models.CharField(max_length=300, blank=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=300, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)


class Piece(models.Model):
    def __str__(self):
        return self.composer + ' ' + self.piece
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    composer = models.CharField(max_length=20, help_text='Surname only')
    piece = models.CharField(max_length=200)
    order = models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')


class Rehearsal(models.Model):
    def __str__(self):
        return self.rehearsal_date
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    rehearsal_date = models.DateTimeField('rehearsal date')
    rehearsal_venue = models.CharField(max_length=300)
    notes = models.CharField(max_length=400, blank=True)


class CommitteeMember(models.Model):
    def __str__(self):
        return self.role + ' (' + self.name + ')' + ' - ' + self.season
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=10, default='2017/18', help_text='Format yyyy/yy')
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    instrument = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    role_description = models.CharField(max_length=1000, help_text="Description provided by personally by the committee member")


class ConcertoWinner(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=300)
    instrument = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)

# Content Manager (for editing page text via admin)
