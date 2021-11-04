from django import forms
from django.contrib.auth import login, authenticate  #automated pre built forms from django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): #RegisterForm is inheriting from UserCreationForm which is a class
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]