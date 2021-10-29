from django.urls import path
from Book import views

urlpatterns=[
    path("list/",views.list_book,name="list"),
    path("add/",views.Add_book,name="bookadd"),
    path("remove/<int:id>",views.remove_book,name="removebook"),
    path("change/<int:id>",views.change_book,name="changebook"),
    path("view/<int:id>",views.book_details,name="bookdetails")
]