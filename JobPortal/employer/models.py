from django.db import models


class Employerprofile(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=40)
    phonenumber=models.CharField(max_length=15)
    company=models.CharField(max_length=120)
    post=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images",null=True)
