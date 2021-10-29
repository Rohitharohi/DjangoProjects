from django import forms
from django.forms import ModelForm
from mobile.models import Mobile

# class Mobileform(forms.Form):
#     mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     ram=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     availability=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"]
#         availability=cleaned_data["availability"]
#
#         if price < 0:
#             msg="invalid price"
#             self.add_error("price",msg)
#
#         if availability < 0:
#             msg="invalid"
#             self.add_error("availability",msg)


class Mobileform(ModelForm):
    class Meta:
        fields=["mobile_name","color","ram","price","availability","image"]
        model=Mobile
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "color":forms.TextInput(attrs={"class":"form-control"}),
            "ram":forms.NumberInput(attrs={"class":"form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "availability": forms.NumberInput(attrs={"class": "form-control"}),

        }
