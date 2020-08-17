from apps.street import views
from django.urls import include, path
from rest_framework import routers

urlpatterns = [
    path("city/street/<int:pk>/", views.StreetDetailCityView.as_view()),

]
