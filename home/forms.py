from django.forms import ModelForm, TextInput
from .models import message_from_about_us
from django import forms


class message_from_about_us_form(ModelForm):
    class Meta:
        model = message_from_about_us
        fields = ["topic", "text"]
        widgets = {
            "topic": TextInput(attrs={"class": "input", "placeholder": "title"}),
            "text": forms.Textarea(
                attrs={"class": "input", "placeholder": "message us . . . ."}
            ),
        }
