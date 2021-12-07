from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm
from django.shortcuts import redirect, render
from .forms import PostForm
from .forms import LogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
from .models import Post


def feed(request):
    return render(request, 'feed.html')

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

def log_out(request):
    logout(request)
    return redirect('home')

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

def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {'list': users})

def show_user(request, user_id):
    user = User.objects.get(username=user_id)
    return render(request, "show_user.html", {'user': user})

def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)
            # post = form.save(False)
            current_user = request.user
            if form.is_valid():
                text = form.cleaned_data.get('text')
                post = Post.objects.create(author=current_user, text=text)
                return redirect('feed')
            else:
                return render(request, 'feed.html', {'form': form})
        else:
            return redirect('log_in')
    return render(request, "new_post.html", {'form': form})

# def new_post(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             current_user = request.user
#             form = PostForm(request.POST)
#             if form.is_valid():
#                 text = form.cleaned_data.get('text')
#                 post = Post.objects.create(author=current_user, text=text)
#                 return redirect('feed')
#             else:
#                 return render(request, 'feed.html', {'form': form})
#         else:
#             return redirect('log_in')
#     else:
#         return HttpResponseForbidden()
