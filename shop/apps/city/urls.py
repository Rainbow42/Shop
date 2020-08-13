from django.urls import include, path
from rest_framework import routers
from apps.city import views

urlpatterns = [
    path("", views.CityListView.as_view()),

]
