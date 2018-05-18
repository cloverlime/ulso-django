from django.urls import path, include

from tastypie.api import Api


from .api import (
                    ConductorResource,
                    ConcertResource,
                    OrchestrationResource,
                    PieceResource
                    )

from . import views

# API resources

conductors = ConductorResource()

v1_api = Api(api_name='v1')
v1_api.register(ConductorResource())
v1_api.register(ConcertResource())
v1_api.register(OrchestrationResource())
v1_api.register(PieceResource())

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(v1_api.urls)),
    path('json/', views.testjson)
]
