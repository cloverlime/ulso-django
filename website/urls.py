from django.urls import path
from django.views.generic import TemplateView

# from ulsosite.views import views
from website.views import views

from website.views.forms import contact
from website.views.forms.absence import AbsenceFormView
from website.views.forms.audition_signup import AuditionSignUpView
from website.views.forms.project_signup_view import ProjectFormView
from website.views.forms.concerto_signup_view import ConcertoSignUp


urlpatterns = [
    path('', TemplateView.as_view(template_name='website/pages/index.html'), name='index'),
    path('whatson/', views.whatson, name='whatson'),
    path('rehearsals/', views.rehearsals, name='rehearsals'),
    path('contact/', contact.contact, name='contact'),
    path('concerto/', views.concerto, name='concerto'),
    # path('auditions/', views.auditions, name='auditions'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('media/', views.media, name='media'),
    # path('committee', views.committee, name='committee'),

    # Forms and signups
    path('auditions/signup/', AuditionSignUpView.as_view(), name='signup'),
    path('absence', AbsenceFormView.as_view(), name='absence'),
    path('project/signup/', ProjectFormView.as_view(), name='project_signup'),
    path('concerto/signup/', ConcertoSignUp.as_view(), name='signup'),
]
