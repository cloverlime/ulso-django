from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from ulsosite.forms import (
                    AuditionSignUp,
                    ContactForm,
                    ConcertoForm,
                    )

from ulsosite.models.concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from ulsosite.models.people import (
                        CommitteeMember,
                        ConcertoWinner,
                        )

from ulsosite.models.cms import (
                        Page,
                        Section,
                        AccordionCard,
                        )


def index(request):
    return HttpResponse("Here is the Index page")

def rehearsals(request):
    page = Page.objects.get(title="Rehearsals")
    current_concert = Concert.objects.get(current=True)
    pieces = current_concert.piece_set.all()
    rehearsals = current_concert.rehearsal_set.all()
    venue = current_concert.venue_set.first()
    # upcoming_concerts = Concert.objects.filter(current=False).order_by('date')
    context = {
                'concert': current_concert,
                'page': page,
                'pieces': pieces,
                'rehearsals': rehearsals,
                'venue': venue
                }
    return render(request, 'ulsosite/rehearsals.html', context)

def contact(request):
    """
    Logic for the website's contact form. Sends an email directly to committee members' role@ulso.co.uk email addresses depending on the topic chosen by the sender.
    """
    if request.method != 'POST':
        page = Page.objects.get(title="Contact Us")
        form = ContactForm()
        committee_member = CommitteeMember.objects.all()
        context = {'committee_members': committee_member,
                   'contact_form': form,
                   'page': page }
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

def about(request):
    page = Page.objects.get(title="About")
    accordion = page.accordioncard_set.all().order_by("order")
    chair = CommitteeMember.objects.get(role="Chair")
    committee = CommitteeMember.objects.all().exclude(role="Chair")
    context = {
    'accordion': accordion,
    'page': page
    }
    return render(request, 'ulsosite/accordion.html', context)

def committee(request):
    page = Page.objects.get(title="Committee")
    chair = CommitteeMember.objects.get(role="Chair")
    committee = CommitteeMember.objects.all().exclude(role="Chair")
    context = {
    'chair': chair,
    'committee': committee
    }
    return render(request, 'ulsosite/committee.html', context)


def join(request):
    page = Page.objects.get(title="How to Join")
    accordion = page.accordioncard_set.all().order_by('order')
    context = {
    'accordion': accordion,
    'page': page
    }
    return render(request, 'ulsosite/accordion.html', context)


def media(request):
    return HttpResponse("ULSO's media page")

def whatson(request):
    page = Page.objects.get(title="What's On")
    current_concert = Concert.objects.get(current=True)
    current_pieces = current_concert.piece_set.all().order_by('order')
    concerts = Concert.objects.exclude(current=True)
    context = {
                'current_concert': current_concert,
                'page': page,
                'current_pieces': current_pieces,
                'concerts': concerts,
                }
    return render(request, 'ulsosite/whatson.html', context)
