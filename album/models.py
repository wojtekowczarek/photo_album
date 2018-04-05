from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField()
    path = models.CharField(max_length=64)
    creation_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User)