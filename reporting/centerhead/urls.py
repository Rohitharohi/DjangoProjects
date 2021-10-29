from django.urls import path
from centerhead import views

urlpatterns = [
    path("",views.home,name="index"),
    path("courses/add",views.add_course,name="courseadd"),
    path("batches/add", views.add_batches,name="batch"),
    path("users/add", views.add_faculty,name="facalty"),
    path("timesheet", views.view_timesheet,name="timesheet"),
    path("accounts/signup",views.Registration,name="registration"),
    path("accounts/signin",views.view_login,name="log"),
    path("batches",views.list_batches,name="listbatches"),
    path("users",views.list_faculty,name="users")

]