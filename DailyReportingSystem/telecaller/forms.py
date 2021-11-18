from django import forms
from telecaller.models import Enquiries

class Loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())

class Enquiryform(forms.ModelForm):
    class Meta:
        model = Enquiries
        # fields=["student_name","contact","email","course","status","followupdate"]
        exclude=("enquirydate","created_by")
        widgets={
            "followupdate":forms.DateInput(attrs={"type":"date"})
        }

class Dateform(forms.Form):
    model = Enquiries
    from_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    to_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))


