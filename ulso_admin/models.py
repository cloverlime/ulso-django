from django.db import models

class Musician(models.Model):

    # YEAR_LIST = ('1','2','3','4','5','6', 'N/A')

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
    ('Other', 'Other university'),
    ('Graduate', 'Graduate'),
    )

    date = models.DateTimeField('date entered')
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default=None) # optional
    email = models.EmailField(max_length=100)
    instrument = models.CharField(max_length=1, choices=INSTRUMENT_LIST)
    doubling = models.CharField(max_length=50, default=None) # optional

    uni = models.CharField(max_length=1, choices=UNI_LIST)
    other_uni = models.CharField(max_length=50, default=None)
    # year = models.CharField(max_length=1, choices=YEAR_LIST)
    returning_member = models.BooleanField(default=False)

    subs_paid = models.BooleanField(default=False)

class Conductor(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100) # change this
    rate_per_hour = models.IntegerField()
    rate_concert_day = models.IntegerField()
    favourite = models.BooleanField(default=False)
