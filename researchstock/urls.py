from django.urls import path
from . import views

urlpatterns = [
    path('', views.logInPage),
    path('index/', views.index, name='index'),
    path('signUpPage/', views.signUpPage, name='signUpPage'),
    path('logInPage/', views.logInPage, name='logInPage'),
    path('signup/', views.signUp, name='signUp'),
    path('login/', views.logIn, name='logIn')
]
