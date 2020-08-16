from apps.shops import views
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path("shop/", views.ShopListView.as_view()),
]
