#coding:utf8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self',related_name='myfriend')
    #friends = models.ManyToManyField('self',related_name='myfriend',symmetrical=True) symmetrical为True 则为飞对称关系
    def __unicode__(self):
        return self.name

class QQGroup(models.Model):
    name = models.CharField(max_length=30)
    founder = models.ForeignKey(UserProfile,related_name='Groups')
    admin = models.ManyToManyField(UserProfile,related_name='GroupAdmin')
    members = models.ManyToManyField(UserProfile,related_name='GroupMembers')
    brife = models.TextField(max_length=30,default='群主很懒')
    maxMember = models.IntegerField(default=200)

    def __unicode__(self):
        return self.name