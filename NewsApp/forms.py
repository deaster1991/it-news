from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


# class NewsForm(forms.Form):
# title = forms.CharField(max_length=150, label='Назва',
#                         widget=forms.TextInput(attrs={"class": "form-control"}))
# content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={"class": "form-control"}))
# is_published = forms.BooleanField(label='Видимість', required=False,
#                                   widget=forms.CheckboxInput(
#                                       attrs={"class": "form-check-input", "type": "checkbox"}))
# category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Розділ',
#                                   empty_label='оберіть категорію',
#                                   widget=forms.Select(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category', ]
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control"}),
            'is_published': forms.CheckboxInput(attrs={"class": "form-check-input", "type": "checkbox"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            # 'photo': forms.FileInput(attrs={"class": "custom-file-input"}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Назва не повинна починатися з цифри')
        return title


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Імя користувача', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Імя користувача', widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Пошта', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
