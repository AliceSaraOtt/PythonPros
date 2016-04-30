from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class cat(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,related_name='cats')
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='articles')
    cat = models.ForeignKey(cat,related_name='cats')

class comment(models.Model):
    content = models.TextField()
    art = models.ForeignKey(Article,related_name='comments')

    def __unicode__(self):
        return self.content