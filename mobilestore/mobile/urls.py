from django.urls import path
from mobile import views

urlpatterns=[

    path("list",views.Listmobile.as_view(),name="mobilelist"),
    path("", views.mobile,name="home"),
    path("add", views.Addmobile.as_view(), name="mobile"),
    path("remove/<int:id>", views.Removemobile.as_view(), name="removemobile"),
    path("change/<int:id>",views.Changemobile.as_view(),name="changemobile"),
    path("details/<int:id>",views.Mobiledetails.as_view(),name="mobiledetails"),
    path("orders/list",views.Vieworders.as_view(),name="customerorders"),
    path("orders/view/<int:id>",views.Viewmobiledetail.as_view(),name="newordermobile"),
    path("orders/update/<int:id>",views.OrderUpdateview.as_view(),name="updateorder"),
    path("findmobile",views.MobileSearch.as_view(),name="searchmobile")


]