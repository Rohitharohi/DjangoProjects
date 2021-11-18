from django.forms import ModelForm
from django import forms
from reportingsystem.models import MyUser

from centerhead.models import Course,Batch

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields=["course_name"]
        widgets={
            "course_name":forms.TextInput(attrs={"class":"form-control"})
        }

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields=["course","batch_name"]
        widgets= {
            "course": forms.Select(attrs={"class": "form-control form-select"}),
            "batch_name": forms.TextInput(attrs={"class": "form-control"})

        }

class UpdateBatch(ModelForm):
    class Meta:
        model = Batch
        fields=["course","batch_name"]
        widgets={
            "course": forms.Select(attrs={"class": "form-control form-select"}),
            "batch_name": forms.TextInput(attrs={"class": "form-control"})
        }

class Updatevourse(ModelForm):
    class Meta:
        model = Course
        fields=["course_name"]
        widgets={
            "course_name:":forms.TextInput(attrs={"class":"form-control"})
        }



class EmployeeForm(ModelForm):
    class Meta:
        model = MyUser
        fields=["email","phonenumber","role","password"]
