from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from app.models import User
from django.urls import reverse_lazy
from app.serializers import UserSerializer
from django.http import JsonResponse

# Create your views here.

class UserSignup(CreateView):
    model=User
    serializer_class=UserSerializer
    success_url=reverse_lazy('user:signup')

    def post(self, request, *args, **kwargs):
        user_data = self.serializer_class(data=request.data)

        if user_data.is_valid():

            user_data.save()
            return JsonResponse(user_data, status=201)
        
        else:
            return JsonResponse(user_data.errors, status=400)

    def get_success_url(self) -> str:
        return self.success_url
    
class UserLogin(LoginView):
    model=User
    success_url=reverse_lazy("user:userprofile")

    def get_success_url(self) -> str:
        return self.success_url
