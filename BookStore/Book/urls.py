from django.urls import path
from Book import views

urlpatterns=[

    path("list/",views.Listbook.as_view(),name="list"),
    path("add/",views.Bookcreateview.as_view(),name="bookadd"),
    path("remove/<int:id>",views.Removebook.as_view(),name="removebook"),
    path("change/<int:id>",views.Bookupdate.as_view(),name="changebook"),
    path("view/<int:id>",views.Bookdetail.as_view(),name="bookdetails"),
    path("order/list",views.Vieworders.as_view(),name="orders"),
    path("order/list/newbook/View/<int:id>",views.Viewneworderedbook.as_view(),name="neworderdbook"),
    path("order/update/<int:id>", views.OrderUpdateview.as_view(),name="updateorder"),

]