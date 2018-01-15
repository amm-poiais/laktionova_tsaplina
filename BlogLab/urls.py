"""BlogLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from Blog.views import *

urlpatterns = [
    url(r'^$', main_page), #главная страница
    url(r'^admin/', admin.site.urls),
    url(r'^moderate[/]?$', moderate),
    url(r'^moderate_news[/]?$', moderate_news),
    url(r'^user_profile[/]?$', user_profile),
    url(r'^create_news[/]?$', create_news),
    url(r'^login[/]?$', login),
    url(r'^error[/]?$', error),
    url(r'^search[/]?$', search),
    #url(r'^search/$', search),
    url(r'^logout[/]?$', log_out),
    url(r'^signup[/]?$', signup),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)