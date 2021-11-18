from django.urls import path
from customer import views
urlpatterns=[
    path('home',views.Customerhome.as_view(),name="customerhome"),
    path('accounts/users/add',views.Signup.as_view(),name="login"),
    path('accounts/users/login', views.Signin.as_view(), name="signin"),
    path('accounts/users/logout', views.signout, name="signout"),
    path('addtocart/<int:id>',views.Addtocart.as_view(),name="addtocart"),
    path('viewmycart',views.Viewmycart.as_view(),name="mycart"),
    path('cart/item/remove/<int:id>',views.RemoveItem.as_view(),name="removeitem"),
    path('books/buynow/<int:id>',views.Ordercreate.as_view(),name="ordercreation"),
    path('books/item/mycart',views.Viewmyorders.as_view(),name="myorders"),
    path('books/remove/<int:id>',views.RemoveOrdereditem.as_view(),name="removeordereditem"),
    path('mobile/find',views.Mobilefindview.as_view(),name="searchmobile")

]