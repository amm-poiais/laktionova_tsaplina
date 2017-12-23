from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.http import HttpResponseRedirect


def login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect('/users')
        else:
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(
            request,
            'login.html',
            {'login_form': form})

