from django.shortcuts import render,render_to_response
from DjangoUeditor.forms import UEditorField
from django import forms

from django.template import loader
# Create your views here.

class TestUEditorForm(forms.Form):
    content = UEditorField('content',initial='success',width=600,height=800)

def add(req):
    form = TestUEditorForm()
    return render(req,'message.html',{'form':form})

