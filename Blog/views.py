from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect
from Blog.models import User
from Blog.models import News


# Create your views here.


def user_profile(request):
    user = request.user
    user_news = News.objects.filter(
        user=user).order_by('-id')
    user_news = [
        {
            'title': user_post.title,
            'text': user_post.text,
            'attachment': user_post.attachment,
            'timestamp': user_post.timestamp,
            'category': user_post.category
        }
        for user_post in user_news
    ]
    return render(
        request,
        'user_profile.html',
        {'user': user,
         'user_news': user_news})

def main_page(request):
    user = request.user
    news = News.objects. filter(
        status__status='Published').order_by('-id')
    news = [
        {
            'title': user_news.title,
            'text': user_news.text,
            'attachment': user_news.attachment,
            'timestamp': user_news.timestamp,
            'category': user_news.category,
            'user': user
        }
        for user_news in news
    ]
    return render(
        request,
        'main.html',
        {'user': user,
         'news': news})


"""
def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
"""


def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect('/users')
            #return HttpResponseRedirect('/main' )
        else:
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(
            request,
            'login.html',
            {'login_form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1')
                                )
            django_login(request, user)
            return redirect('/users')
            #return redirect('/main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'logout.html')

