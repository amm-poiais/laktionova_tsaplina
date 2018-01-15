from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect
from Blog.models import NewsStatus
from Blog.models import News
from Blog.forms import NewsForm, SearchForm, ModerateForm
import datetime


# Create your views here.


def user_profile(request):
    user = request.user
    user_news = News.objects.filter(user=user).order_by('-id')
    user_news = [
        {
            'title': user_post.title,
            'text': user_post.text,
            'attachment': user_post.attachment,
            'timestamp': user_post.timestamp,
            'category': user_post.category,
            'status': user_post.status,
            'comment': user_post.comment
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
    news = News.objects.filter(status__status='Published').order_by('-id')
    news = [
        {
            'title': user_news.title,
            'text': user_news.text,
            'attachment': user_news.attachment,
            'timestamp': user_news.timestamp,
            'category': user_news.category,
            'user': user_news.user
        }
        for user_news in news
    ]
    return render(
        request,
        'main.html',
        {'user': user,
         'news': news})


def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect('/')
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
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('/')


def create_news(request):
    if request.method == 'POST':
        fm = NewsForm(request.POST, request.FILES)
        if fm.is_valid():
            news = News()
            news.user_id = request.user.id
            news.title = fm.cleaned_data['title']
            news.text = fm.cleaned_data['text']
            news.attachment = fm.cleaned_data['attachment']
            news.timestamp = datetime.datetime.now()
            news.status = NewsStatus.objects.get(status='Pending')
            news.category_id = fm.cleaned_data['category'].id
            news.save()
            return redirect('/')
    else:
        fm = NewsForm()
    return render(
        request,
        'create_news.html',
        {'fm': fm})


def error(request):
    return render(
        request,
        'error.html')


def search(request):
    res_list = None
    if request.method == 'POST':
        flag = False
        fm = SearchForm(request.POST, request.FILES)
        if fm.is_valid():
            if fm.cleaned_data['options'] == 'category':
                ctg = fm.cleaned_data['category']
                res_list = News.objects.filter(category=ctg,
                                               status__status='Published')
            else:
                p_d = fm.cleaned_data['pub_date']
                res_list = News.objects.filter(timestamp__year=p_d.year,
                                               timestamp__month=p_d.month,
                                               timestamp__day=p_d.day,
                                               status__status='Published')
    else:
        fm = SearchForm()
        flag = True
    return render(
        request,
        'search.html',
        {'fm': fm,
         'search': flag,
         'res_list': res_list})


def moderate(request):
    if not request.user.is_staff:
        return error(request)
    news_list = News.objects.filter(status__status='Pending').order_by('-id')
    fm = ModerateForm()
    return render(
        request,
        'moderate.html',
        {'news': news_list,
         'fm': fm})


def moderate_news(request):
    if request.method == 'POST':
        fm = ModerateForm(request.POST)
        if fm.is_valid():
            post = News.objects.get(id=request.GET['news_id'])
            if fm.cleaned_data['actions'] == 'publish':
                post.status = NewsStatus.objects.get(status='Published')
            else:
                post.status = NewsStatus.objects.get(status='Rejected')
                post.comment = fm.cleaned_data['comment']
            post.save()
        return redirect('/moderate')
    else:
        post = News.objects.get(id=request.GET['news_id'])
        fm = ModerateForm()
        return render(
            request,
            'moderate_news.html',
            {'post': post,
             'fm': fm})
