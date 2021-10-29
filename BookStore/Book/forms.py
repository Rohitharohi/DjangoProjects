from django import forms
from django.forms import ModelForm
from Book.models import Book

# class Bookform(forms.Form):
#     book_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     author=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     availability=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#
#
#     def clean(self):
#         cleaned_data=super().clean()
#         price=cleaned_data["price"]
#         availability=cleaned_data["availability"]
#
#         if price<0:
#             msg="invalid price"
#             self.add_error("price",msg)
#
#         if availability<0:
#             msg="invalid"
#             self.add_error("availability",msg)


class Bookform(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies","image"]
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "copies": forms.NumberInput(attrs={"class": "form-control"}),


        }
