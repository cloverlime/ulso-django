from django.db import models

YEAR_LIST = (
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
('N/A','N/A'),
)

INSTRUMENT_LIST = (
('Flute', 'Flute'),
('Clarinet', 'Clarinet'),
('Oboe', 'Oboe'),
('Bassoon','Bassoon'),
('Horn', 'Horn'),
('Trumpet', 'Trumpet'),
('Trombone', 'Trombone'),
('Tuba', 'Tuba'),
('Violin', 'Violin'),
('Viola', 'Viola'),
('Cello', 'Cello'),
('Bass', 'Bass'),
('Timpani & Percussion', 'Timpani & Percussion'),
('Harp','Harp'),
)

UNI_LIST = (
('RCM', 'Royal College of Music'),
('RAM', 'Royal Academy of Music'),
('Trinity', 'Trinity Laban Conservatoire'),
('GSMD', 'Guildhall School of Music and Drama'),
('KCL', 'King\'s College London'),
('UCL', 'University College London'),
('ICL', 'Imperial College London'),
('LSE', 'London School of Economics'),
('RVC', 'Royal Veterinary College'),
('SOAS', 'SOAS'),
('RH', 'Royal Holloway'),
('City', 'City, University of London'),
('Goldsmiths', 'Goldsmiths, University of London'),
('LSHTM', 'London School of Hygiene and Tropical Medicine'),
('BK', 'Birkbeck'),
('QMUL', 'Queen Mary University of London'),
('Graduate', 'Graduate'),
('Other', 'Other'),
)

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
    year = models.CharField(max_length=1, choices=YEAR_LIST, blank=True)
    experience = models.TextField(default='Briefly summarise your recent orchestral experience')
    returning_member = models.BooleanField(default=False)
    subs_paid = models.BooleanField(default=False)


class ConcertoApplicant(Person):
    # date = models.DateTimeField('date submitted')
    year = models.CharField(max_length=1, choices=YEAR_LIST)
    pieces = models.TextField()
    years_ulso_member = models.CharField(max_length=30)
    notes = models.TextField(blank=True)


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
        return self.name
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100) # change this
    rate_per_hour = models.IntegerField()
    rate_concert_day = models.IntegerField()
    notes = models.TextField()
