from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from . import forms
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'signup.html'

def thanksview(request):
    return render(request, 'thanks.html')
