from django.db import models
from django.contrib.auth.models import User

'''
Creating a post model from lesson 6 instructions
'''


class Post(models.Model):
    title = models.Charfield(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
