from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class booklibForm(forms.ModelForm):
    class Meta:
        model = booklib
        fields = ['name', 'contact', 'booktitle', 'bookauthor','yearpub','bookgenre', 'radio_choice', 'booksummary']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']