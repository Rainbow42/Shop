from django.urls import include, path
from rest_framework import routers
from apps.shops import views

urlpatterns = [
  #  path("shop/", views.ShopListView.as_view()),
    path("shop/", views.ShopCreateView.as_view()),

]
