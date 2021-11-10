from django.db import models
from django.contrib.auth.models import Group
# Create your models here.



class Message(models.Model):
    username=models.CharField(max_length=200)
    room = models.CharField(max_length=255)
    content =models.TextField()
    created_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username