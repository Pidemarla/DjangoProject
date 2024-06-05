from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth 
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def index(request):
    
    # dests = Destination.objects.all()

    # return render(request, 'index.html', {'dests' : dests})
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('index')

def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else: 
        return render(request, 'login.html')

def signup(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']    
        password2 = request.POST['confirm_password']

        if password1 != password2:
            # Passwords don't match, handle the error
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        try:
            user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
            user.save()
            return render(request, 'login.html')
        except IntegrityError:
            # Handle the case where the username or email already exists
            return render(request, 'register.html', {'error': 'Username or email already exists'})

    
    else:
        return render(request, 'register.html')