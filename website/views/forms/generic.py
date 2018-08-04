from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

class GenericFormView(View):
    form_class = None
    form_template = 'website/forms/form.html'
    success_template = 'website/forms/form-success.html'
    form_title = ''

    def get(self, request, *args, **kwargs):
        title = self.form_title
        form = self.form_class()
        context = {
            'form': form,
            'title': title
        }
        return render(request, self.form_template , context)

    def post(self, request, *args, **kwargs):
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            context = {'message': 'Your form was successfully submitted.'}
            return render(request, self.success_template, context)
        else:
            return HttpResponse("Form wasn't valid")

    class Meta:
        abstract = True
