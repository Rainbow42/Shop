from apps.city import views
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path("city/", views.CityListView.as_view()),

]
