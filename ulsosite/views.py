from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from .forms import (
                    AuditionSignUp,
                    ContactForm,
                    ConcertoForm,
                    )

from ulsosite.models.models_concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from ulsosite.models.models_people import (
                        CommitteeMember,
                        ConcertoWinner,
                        )

def index(request):
    return HttpResponse("Here is the Index page")

def whatson(request):
    return HttpResponse("Here is the whatson page")

def rehearsals(request):
    current_concert = Concert.objects.filter(current=True)
    upcoming_concerts = Concert.objects.filter(current=False).order_by('concert_date')
    context = {'upcoming_concerts': upcoming_concerts, 'current_concert': current_concert}
    return render(request, 'ulsosite/rehearsals.html', context)

def contact(request):
    """
    Logic for the website's contact form. Sends an email directly to committee members' role@ulso.co.uk email addresses depending on the topic chosen by the sender.
    """
    if request.method != 'POST':
        form = ContactForm()
        committee_members = CommitteeMember.objects.all()
        context = {'committee_members': committee_members, 'contact_form': form }
        return render(request, 'ulsosite/contact.html', context)

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            topic = form.cleaned_data['topic']
            full_subject = topic + ': ' + form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_self = form.cleaned_data['send_self']
            recipients = ['chair@ulso.co.uk']
            contact_address_dict = {
                                'Auditions': ['orchestra.manager@ulso.co.uk'],
                                'Late/Absent': ['orchestra.manager@ulso.co.uk'],
                                'Percussion hire': ['orchestra.manager@ulso.co.uk', 'treasurer@ulso.co.uk'],
                                'Conducting': [],
                                'Concerto': ['orchestra.manager@ulso.co.uk'],
                                'Publicity': ['publicity@ulso.co.uk'],
                                'Sponsorship': ['treasurer@ulso.co.uk', 'sponsorship@ulso.co.uk'],
                                'Concert Queries': ['orchestra.manager@ulso.co.uk'],
                                'Subs': ['treasurer@ulso.co.uk'],
                                'Website':['webmaster@ulso.co.uk'],
                                'Other': []
                                }
            recipients += contact_address_dict[topic]

            if send_self:
                cc_self = [email]
            else:
                cc_self=None

            email_msg = EmailMessage(full_subject, message, from_email=email, to=recipients, cc=cc_self)

            try:
                email_msg.send()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            # Redirect back to contacts page with a suggess message; NEED TO CHANGE THE BELOW
            return redirect(reverse('rehearsals'))

        # Form is not valid
        else:
            return HttpResponse("Invalid form")

def concerto(request):
    return HttpResponse("Here is the page for the concerto competition")

def signup(request):
    form = SignUp()
    context = {'form': form}
    return render(request, 'ulsosite/signup.html', context)
    # return HttpResponse("Here is the page for signing up for an audition")

class SignUpView(View):
    form_class = AuditionSignUp
    form_template = 'ulsosite/signup.html'
    success_template = 'ulsosite/signup-success.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = { 'form': form }
        return render(request, self.form_template , context)

    def post(self, request, *args, **kwargs):
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.success_template)
        else:
            return HttpResponse("Form wasn't valid")

class ConcertoSignUp(SignUpView):
    form_class = ConcertoForm

def signup_success(request):
    return HttpResponse("Thank you for signing up. We will get back to you soon.")


def auditions(request):
    return HttpResponse("Here is the page for info about auditions!")
