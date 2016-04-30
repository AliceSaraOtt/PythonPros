from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cat(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User,related_name='cats')

    def __unicode__(self):
        return self.name

class article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='articles')
    cats = models.ForeignKey(cat,related_name='cats')

    def __unicode__(self):
        return self.title

class comment(models.Model):
    comt = models.TextField()
    art = models.ForeignKey(article,related_name='comments')

    def __unicode__(self):
        return self.comt