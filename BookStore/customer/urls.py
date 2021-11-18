from django.urls import path
from customer import views


urlpatterns=[
    path('home',views.CustomerHome.as_view(),name="customerhome"),
    path('accounts/users/add',views.Signupview.as_view(),name="signup"),
    path('accounts/users/login',views.Signinview.as_view(),name="signin"),
    path('accounts/users/logout', views.signout, name="signout"),
    path('addtocart/<int:id>',views.Addtocart.as_view(),name="addtocart"),
    path('viewmycart/',views.Viewmycart.as_view(),name="viewmycart"),
    path('carts/item/remove/<int:id>',views.Removeitemformcart.as_view(),name="removeitem"),
    path('books/Buynow/<int:id>',views.Ordercreate.as_view(),name="order"),
    path('books/myorders',views.Viewmyorder.as_view(),name="myorders"),
    path('book/myorders/remove/<int:id>',views.RemoveOrderedItem.as_view(),name="removeordereditem"),
    path('find',views.Bookfindview.as_view(),name="findbook")
]