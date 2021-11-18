from django.urls import path
from converter import views

urlpatterns=[

    path('add',views.Converter.as_view(),name="word"),
    # path('ad', views.Converter.as_view(), name="words")

]