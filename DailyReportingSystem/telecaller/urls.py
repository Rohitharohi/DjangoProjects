from django.urls import path
from telecaller import views
urlpatterns=[
    path("login",views.Signinview.as_view(),name="login"),
    path("logout",views.Signout,name="logout"),
    path("enquiries/add",views.EnquiryCreateView.as_view(),name="enquiries"),
    path("home",views.home,name="home"),
    path("followups",views.Followups.as_view(),name="followups"),
    path("enquiries/list",views.Listenquiries.as_view(),name="list"),
    path("reports",views.ViewReports.as_view(),name="report"),


]