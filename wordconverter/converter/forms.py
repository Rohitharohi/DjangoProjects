from django import forms


class Converter(forms.Form):
    number=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
