
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re

class RegisterForm(UserCreationForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        label="Full Name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"})
    )
    mobile = forms.CharField(
        max_length=10,
        required=True,
        label="Mobile Number",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "10-digit mobile number"})
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Re-enter password"})
    )

    class Meta:
        model = User
        fields = ["name", "mobile", "email", "password1", "password2"]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not re.match(r"^[A-Za-z ]+$", name):
            raise forms.ValidationError("Name must contain only letters and spaces.")
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if not re.match(r"^\d{10}$", mobile):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  # use email as username
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["name"]
        if commit:
            user.save()
        return user

