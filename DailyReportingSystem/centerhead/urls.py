from django.urls import path
from centerhead import views

urlpatterns = [
    path("",views.Adminhome.as_view(),name="centerheadhome"),
    path("courses/add",views.Courseadd.as_view(),name="coursedd"),
    path("batches/add",views.Batchadd.as_view(),name="batchadd"),
    path("batches/update/<int:id>",views.Updatebatch.as_view(),name="updatebatch"),
    path("courses/update/<int:id>", views.Updatecourse.as_view(), name="updatecourse"),
    path("add", views.Employees.as_view(), name="employees")

    # path("courses/list",views.Courses.as_view(),name="listcourses")
]
