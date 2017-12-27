from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    attachment = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    status = models.ForeignKey('NewsStatus', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)

    def publish(self):
        self.timestamp = timezone.now()
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NewsStatus(models.Model):
    status = models.CharField(max_length=15)

