from tastypie.resources import ModelResource
from tastypie import fields


from .models import (
                        Musician,
                        Conductor,
                        ConcertoApplicant,
                        ConcertoWinner,
                        CommitteeMember,
                        )

from ulsosite.models import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

class ConductorResource(ModelResource):
    class Meta:
        queryset = Conductor.objects.all()
        resource_name = 'conductors'
        excludes = ['id', 'rate_concert_day', 'rate_per_rehearsal']

class ConcertResource(ModelResource):
    conductor = fields.ForeignKey(ConductorResource, 'conductor')
    class Meta:
        queryset = Concert.objects.all()
        resource_name = 'concerts'
        excludes = ['id', 'current']

class OrchestrationResource(ModelResource):
    class Meta:
        queryset = Piece.objects.all()
        resource_name = 'orchestrations'
        excludes = ['id']

class PieceResource(ModelResource):
    class Meta:
        queryset = Piece.objects.all()
        resource_name = 'pieces'
        includes = ['composer', 'piece']
