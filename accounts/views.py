from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView


# Create your views here.
class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    
class LoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
class UserLogoutView(LoginView):
    pass