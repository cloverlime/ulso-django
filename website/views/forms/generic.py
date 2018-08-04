from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

class GenericFormView(View):
    form = None
    form_template = 'website/forms/form.html'
    success_template = 'website/forms/form-success.html'
    form_title = ''
    success_message = 'Your form was successfully submitted.'

    def get(self, request, *args, **kwargs):
        title = self.form_title
        form = self.form
        context = {
            'form': form,
            'title': title
        }
        return render(request, self.form_template , context)

    def post(self, request, *args, **kwargs):
        form = None
        if form.is_valid():
            form.save()
            context = {'message': self.success_message }
            return render(request, self.success_template , context)
        else:
            return HttpResponse("Form wasn't valid")

    class Meta:
        abstract = True
