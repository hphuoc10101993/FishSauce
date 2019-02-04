from django import forms

from FishSauceApp.models import FishSauce, Company


class FishSauceForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        exclude = []
        model = FishSauce


class CompanyForm(forms.ModelForm):
    class Meta:
        exclude = []
        model = Company