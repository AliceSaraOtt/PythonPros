#coding:utf8
from django.db import models
from DjangoUeditor.models import UEditorField
from django import forms
from DjangoUeditor.widgets import UEditorWidget

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True)
    content = UEditorField(u'内容',width=600,height=300,toolbars='full',imagePath='',filePath='',upload_settings={'imangeMaxSize':1204000},
                           settings={},command=None,blank=True)


