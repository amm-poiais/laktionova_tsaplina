from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    attachment = models.ImageField(upload_to='user', blank=True, null=True)
    status = models.ForeignKey('NewsStatus', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)

    def publish(self):
        self.timestamp = timezone.now()
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=50)


class NewsStatus(models.Model):
    status = models.CharField(max_length=15)

