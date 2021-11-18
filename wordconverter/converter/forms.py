from django import forms


class Converterform(forms.Form):
    number=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
