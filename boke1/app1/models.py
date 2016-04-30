from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cat(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,related_name='cat')
    def __unicode__(self):
        return self.name

class article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='article')
    cat = models.ForeignKey(cat,related_name='cat')

class comment(models.Model):
    art = models.ForeignKey(article,related_name='comments')
    content = models.TextField()
    def __unicode__(self):
        return self.content
