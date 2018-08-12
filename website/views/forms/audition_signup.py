from django.shortcuts import render, redirect

from website.views.forms.generic import GenericFormView
from website.forms.audition_signup import AuditionSignUpForm

class AuditionSignUpView(GenericFormView):
    form = AuditionSignUpForm()
    form_title = "Audition Sign-Up"
    success_message = "Thank you for signing up to ULSO."

    def post(self, request, *args, **kwargs):
        form = AuditionSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': self.success_message }
            return render(request, self.success_template , context)
        else:
            return HttpResponse("Form wasn't valid")
            
