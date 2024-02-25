from django.urls import path
from app import views

app_name="app"
urlpatterns=[
    path("signup/",views.UserSignup.as_view(), name="signup"),
    path("login/",views.UserLogin.as_view(),name="login"),
]