from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from django.shortcuts import redirect, render
from .forms import PostForm
from .forms import LogInForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

def feed(request):
    form = PostForm()
    return render(request, 'feed.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('feed')
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def home(request):
    return render(request, "home.html")

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {'form': form})
