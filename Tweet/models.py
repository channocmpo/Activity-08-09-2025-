from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='tweets/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.content[:50]

