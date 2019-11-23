from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User_details


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class User_detailsForm(forms.ModelForm):
    #############################################choices##################################
    year_list = [("1st", "1st"), ("2nd", "2nd"), ("3rd", "3rd"), ("4th", "4th")]
    branch_list = [
        ("Computer Science & Engineering", "Computer Science & Engineering"),
        ("Electronic Engineering", "Electronic Engineering"),
        ("Industrial & Production Engineering", "Industrial & Production Engineering"),
        ("Electrical Engineering", "Electrical Engineering"),
        ("Civil Engineering", "Civil Engineering"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        (
            "Instrumentation and Control Engineering",
            "Instrumentation and Control Engineering",
        ),
        ("Applied Science and Humanity", "Applied Science and Humanity"),
        ("Management", "Management"),
    ]
    #####################################################################################
    phone_no = forms.CharField(max_length=20, required=False)
    branch = forms.CharField(
        max_length=400,
        label="select your branch",
        widget=forms.Select(choices=branch_list),
        required=False,
    )
    roll_no = forms.CharField(max_length=30, required=False)
    year = forms.CharField(
        max_length=5,
        label="select your year",
        widget=forms.Select(choices=year_list),
        required=False,
    )
    date_of_birth = forms.DateTimeField(required=False)

    class Meta:
        model = User_details
        fields = ["phone_no", "roll_no", "branch", "year", "date_of_birth"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
