from django.contrib import admin

# Register your models here.

from mobile.models import Mobile,Cart

admin.site.register(Mobile)
admin.site.register(Cart)