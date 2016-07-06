from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('name', 'city', 'street', 'postal_code', 'number')
