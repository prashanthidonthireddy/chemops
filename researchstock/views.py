from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.
def index(request):
    return render(request, "researchstock/base.html/")


def logInPage(request):
    return render(request, "researchstock/loginPage.html/")


def logIn(request):
    if request.method == 'POST':
        myusername = request.POST['loginusername']
        mypassword = request.POST['loginpassword']

        user = authenticate(username=myusername, password=mypassword)

        if user is not None:
            login(request, user)
            messages.info(request, 'Login successful')
            return redirect('index')

        else:
            messages.info(request, 'Invalid username and password')
            return redirect('logInPage')

    else:
        return HttpResponse('404-PAGE NOT FOUND')

def signUpPage(request):
    return render(request, "researchstock/signUpPage.html/")

def signUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        userRole = request.POST['userRole']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1!=password2:
            messages.info(request, 'Password1 and Password2 are different')
            return redirect('signUpPage')

        elif User.objects.filter(username=username).exists():
            messages.info(request, 'This username already exist')
            return redirect('signUpPage')

        else:
            users = User.objects.create_user(username=username, password=password1, email=email, first_name=firstName, last_name=lastName)
            users.save()
            profile = Profile(user = request.user, userRole=userRole)
            profile.save()
            messages.info(request, 'Your urco account is successfully created')
            return redirect('signUpPage')
    else:
        return HttpResponse('404-page NOT FOUND')