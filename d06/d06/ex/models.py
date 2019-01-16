from django.db import models
from django.contrib.auth.models import AbstractUser


class TipUser(AbstractUser):
    pass


class Upvotes(models.Model):
    vote_user = models.CharField(max_length=128)


class Downvotes(models.Model):
    vote_user = models.CharField(max_length=128)


class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(Upvotes)
    downvotes = models.ManyToManyField(Downvotes)


