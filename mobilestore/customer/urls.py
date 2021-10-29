from django.urls import path
from customer import views
urlpatterns=[
    path('home',views.customer_home,name="customerhome"),
    path('accounts/users/add',views.sign_up,name="login"),
    path('accounts/users/login', views.signin, name="signin"),
    path('accounts/users/logout', views.signout, name="signout"),

]