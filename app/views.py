from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from app.models import User
from django.urls import reverse_lazy
from app.serializers import UserSerializer
from app.serializers import LoginSerializer
from django.http import JsonResponse
from django.contrib.auth import authenticate

# Create your views here.

class UserSignup(CreateView):
    model=User
    serializer_class=UserSerializer
    success_url=reverse_lazy('user:signup')

    def post(self, request, *args, **kwargs):
        user_data = self.serializer_class(data=request.data)

        if user_data.is_valid():

            if User.objects.get(username=user_data.validated_data["username"]).exists():
                return JsonResponse({'error': "User with this username already exists"}, status=400)
        
        else:
            return JsonResponse(user_data.errors, status=400)

    def get_success_url(self) -> str:
        return self.success_url
    
class UserLogin(LoginView):
    model=User
    success_url=reverse_lazy("user:userprofile")

    def post(self, request, *args, **kwargs):
        # although we are not using *args, **kwargs here in post method but 
        # it is a good practice to maintain consistency
        user_data=LoginSerializer(data=request.data)

        if user_data.is_valid():
            username = user_data.validated_data['username']
            password = user_data.validated_data['password']

            user=authenticate(request,username=username, password=password)
            if user is not None:
                pass

    def get_success_url(self) -> str:
        return self.success_url
