from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm



def Home(request):
    return render(request, 'Home.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Button')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
            return redirect('Login')
        else:
            return HttpResponse('Passwords do not match')
    return render(request, 'Register.html')


@login_required
def Form(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # Process the form data
            # For example, send an email, save to the database, etc.
            return redirect('submit')
    else:
        form = ApplicationForm()

    return render(request, 'Form.html', {'form': form})

def Button(request):
    return render(request, 'button.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('Register')

def submit(request):
    return render(request, 'submit.html')

def contact(request):
    return render(request, 'contact.html')