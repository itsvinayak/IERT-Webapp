from .models import new_by_viewer,Comment
from django.forms import ModelForm,TextInput
from django import forms

class user_news_story(ModelForm):
    date=forms.DateTimeField(required=False,widget=forms.SelectDateWidget)
    class Meta:
        model= new_by_viewer
        fields=['title','image','date','author','info']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
