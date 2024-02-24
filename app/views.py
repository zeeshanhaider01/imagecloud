from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from app.models import User
from django.urls import reverse_lazy

# Create your views here.

class UserSignup(CreateView):
    model=User
    success_url=reverse_lazy('user:signup')

    def get_success_url(self) -> str:
        return self.success_url
    
class UserLogin(LoginView):
    model=User
    success_url=reverse_lazy("user:userprofile")

    def get_success_url(self) -> str:
        return self.success_url
