from django.contrib import admin

# Register your models here.
from portal.models import MyUser
admin.site.register(MyUser)