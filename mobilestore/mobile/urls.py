from django.urls import path
from mobile import views

urlpatterns=[
    path("list",views.list_mobile,name="mobilelist"),
    path("", views.mobile,name="home"),
    path("add", views.Add_mobile, name="mobile"),
    path("remove/<int:id>", views.remove_mobile, name="removemobile"),
    path("change/<int:id>",views.change_mobile,name="changemobile"),
    path("details/<int:id>",views.mobile_details,name="mobiledetails")


]