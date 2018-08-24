"""
All common QuerySets for ULSO admin models are coded here.
"""

from django.db import models
from .people import *



# Musician Managers -------------------

# class MusicianManager(models.Manager):
#     def create_instance(self, attr):
#         """
#         Creates and saves a new model instance given 
#         all the field values in the dictionary attr.
#         """
#         try:
#             musician = self.create(
#                 first_name=attr['first_name'],
#                 last_name=attr['last_name'], 
#                 email=attr['email'],
#                 phone=attr['phone'],
#                 instrument=attr['instrument'], 
#                 doubling=attr['doubling'], 
#                 uni=attr['uni'],
#                 other_uni=attr['other_uni'], 
#                 year=attr['year'], 
#                 experience=attr['experience'], 
#                 returning_member=attr['returning_member'], 
#                 depping_policy=attr['depping_policy'], 
#                 privacy_policy=attr['privacy_policy'],
#             )
#             return musician
#         except:
#             return None





class MemberManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(status='Member')

class ReserveManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(status='Reserve')

class RejectedManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(status='Rejected')

class CandidateManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(status="Candidate")

class WindManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(
                                        Q(instrument='Flute') |
                                        Q(instrument='Clarinet') |
                                        Q(instrument='Oboe') |
                                        Q(instrument='Bassoon')
                                            )

class BrassManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(
                                        Q(instrument='Horn') |
                                        Q(instrument='Trumpet') |
                                        Q(instrument='Trombone (Tenor)') |
                                        Q(instrument='Trombone (Bass)') |
                                        Q(instrument='Tuba')
                                            )

class StringsManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(
                                        Q(instrument='Violin') |
                                        Q(instrument='Viola') |
                                        Q(instrument='Cello') |
                                        Q(instrument='Bass')
                                            )

class PercussionManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(instrument='Percussion')


class HarpsManager(models.Manager):
    def query_set(self):
        return super().get_queryset().filter(instrument='Harp')

# Concerto Audition Managers ------------- Not sure if necessary

# class NoSecondRoundManager(models.Manager):
#     def query_set(self):
#         return super().get_queryset().filter(second_round=False)

# class SecondRoundManager(models.Manager):
#     def query_set(self):
#       return super().get_queryset().filter(second_round=True)
