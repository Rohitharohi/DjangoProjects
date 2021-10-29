from django.urls import path
from reporting import views

urlpatterns = [
    path("courses/add",views.add_courses),
    path("batches/add",views.add_batches),
    path("users/add",views.add_faculty),
    path("timesheet",views.view_timesheets)

]