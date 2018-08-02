from django.urls import path
from django.views.generic import TemplateView

# from ulsosite.views import views
from website.views import views
# from ulsosite.views.views import SignUpView, ConcertoSignUp

urlpatterns = [
    path('', TemplateView.as_view(template_name='ulsosite/index.html'), name='index'),
    path('whatson/', views.whatson, name='whatson'),
    path('rehearsals/', views.rehearsals, name='rehearsals'),
    path('contact/', views.contact, name='contact'),
    path('concerto/', views.concerto, name='concerto'),
    path('auditions/', views.auditions, name='auditions'),
    path('about/', views.about, name='about'),
    path('join/', views.join, name='join'),
    path('media/', views.media, name='media'),
    # path('auditions/signup/', SignUpView.as_view(), name='signup'),
    # path('concerto/signup/', ConcertoSignUp.as_view(), name='signup'),
    path('committee', views.committee, name='committee'),
]
