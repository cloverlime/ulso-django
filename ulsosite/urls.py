from django.urls import path

from ulsosite import views
from ulsosite.views import SignUp, ConcertoSignUp

urlpatterns = [
    path('', views.index, name='index'),
    path('whatson/', views.whatson, name='whatson'),
    path('rehearsals/', views.rehearsals, name='rehearsals'),
    path('contact/', views.contact, name='contact'),
    path('concerto/', views.concerto, name='concerto'),
    path('auditions/', views.auditions, name='auditions'),
    path('auditions/signup/', SignUp.as_view(), name='signup'),
    path('concerto/signup/', ConcertoSignUp.as_view(), name='signup'),
]
