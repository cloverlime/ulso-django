from django.urls import path
from django.views.generic import TemplateView

# from ulsosite.views import views
from website.views import views
from website.views.forms import (
    absence,
    contact,
)
from website.views.forms.absence import AbsenceFormView
from website.views.forms.audition_signup import AuditionSignUpView
# from ulsosite.views.views import SignUpView, ConcertoSignUp

urlpatterns = [
    path('', TemplateView.as_view(template_name='website/index.html'), name='index'),
    path('whatson/', views.whatson, name='whatson'),
    path('rehearsals/', views.rehearsals, name='rehearsals'),
    path('contact/', contact.contact, name='contact'),
    path('concerto/', views.concerto, name='concerto'),
    # path('auditions/', views.auditions, name='auditions'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('media/', views.media, name='media'),
    path('auditions/signup/', AuditionSignUpView.as_view(), name='signup'),
    # path('concerto/signup/', ConcertoSignUp.as_view(), name='signup'),
    path('committee', views.committee, name='committee'),
    path('absence', AbsenceFormView.as_view(), name='absence')
]
