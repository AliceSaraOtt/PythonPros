from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    friend = models.ManyToManyField('self',related_name='myfriend')

    def __unicode__(self):
        return self.name

class QQGroup(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(userProfile,related_name='GroupMember')

    def __unicode__(self):
        return self.name