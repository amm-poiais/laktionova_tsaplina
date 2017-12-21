from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    user = models.ForeignKey('UserProfile', related_name='author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    attachment = models.BinaryField()
    accepted = models.BooleanField()
    comment = models.CharField(max_length=255)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Username: %s; email: %s' % (self.user.username, self.user.email)


class Category(models.Model):
    name = models.CharField(max_length=50)
