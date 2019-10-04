from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Blog_Admin(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    content = models.TextField()

