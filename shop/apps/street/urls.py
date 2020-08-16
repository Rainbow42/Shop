from django.urls import include, path
from rest_framework import routers

from apps.street import views

urlpatterns = [
    path("city/street/<int:pk>/", views.StreetDetailCityView.as_view()),

]
