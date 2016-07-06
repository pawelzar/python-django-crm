from django import forms
from django.contrib.auth.models import User
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'city', 'street', 'postal_code', 'number')


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
