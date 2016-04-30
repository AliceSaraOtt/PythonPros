from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=20)
    friend = models.ManyToManyField('self',related_name='friends',blank=True)

    def __unicode__(self):
        return self.name

class QQgroup(models.Model):
    name = models.CharField(max_length=20)
    member = models.ManyToManyField(UserProfile,related_name='members')

    def __unicode__(self):
        return self.name