from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whatson/', views.whatson, name='whatson'),
    path('rehearsals/', views.rehearsals, name='rehearsals'),
    path('contact/', views.contact, name='contact'),
    path('concerto/', views.concerto, name='concerto'),
]
