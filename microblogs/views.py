from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from django.shortcuts import redirect, render
from .forms import PostForm
from .forms import LogInForm

def feed(request):
    form = PostForm()
    return render(request, 'feed.html', {'form': form})

def log_in(request):
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def home(request):
    return render(request, "home.html")

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {'form': form})
