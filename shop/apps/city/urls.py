from django.urls import include, path
from rest_framework import routers
from apps.city import views

urlpatterns = [
    path("city/", views.CityListView.as_view()),

]
