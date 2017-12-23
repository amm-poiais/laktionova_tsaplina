from django.shortcuts import render
from django.contrib.auth.models import User

from django import forms
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

# Create your views here.
from Blog.models import News


def user_profile(request):
    user_id = request.GET.get('user_id', 3)
    user = User.objects.get(pk=user_id)
    user_news = News.objects.filter(
        user=user).order_by('-id')
    user_news = [
        {
            'title': user_post.title,
            'text': user_post.text,
            'attachment.url': user_post.attachment.url,
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



