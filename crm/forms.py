from django import forms
from django.contrib.auth.models import User
from .models import Company
import re


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'city', 'street', 'postal_code', 'number')

    def clean_postal_code(self):
        cd = self.cleaned_data
        code = cd.get('postal_code')

        if not re.match(r'\d{2}-\d{3}', code):
            raise forms.ValidationError("Should look like this 00-000.")

        return code

    def clean_number(self):
        cd = self.cleaned_data
        number = cd.get('number')

        if not str(number).isnumeric() and len(number) != 10:
            raise forms.ValidationError("Must consist of 10 digits.")

        return number


class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser')
