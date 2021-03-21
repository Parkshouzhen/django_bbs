from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm): # UserCreationForm 상속 받음
    email = forms.EmailField(label="이메일")
    
    class Meta: # Form 만들 때 메타클래스 필요
        model = User
        fields = ("username", "email")