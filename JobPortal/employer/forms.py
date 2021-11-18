from django import forms
from django.forms import ModelForm
from employer.models import Employerprofile

class Profileform(ModelForm):
    class Meta:
        model = Employerprofile
        fields=["name","email","phonenumber","company","post","image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "phonenumber": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "post": forms.TextInput(attrs={"class": "form-control"})

        }
