from django.urls import path
from customer import views


urlpatterns=[
    path('home',views.CustomerHome.as_view(),name="customerhome"),
    path('accounts/users/add',views.Signupview.as_view(),name="signup"),
    path('accounts/users/login',views.Signinview.as_view(),name="signin"),
    path('accounts/users/logout', views.signout, name="signout"),
    path('addtocart/<int:id>',views.Addtocart.as_view(),name="addtocart"),
    path('viewmycart/',views.Viewmycart.as_view(),name="viewmycart")
]