from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, ThingsListView, ThingDetailsView

urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('things',ThingsListView.as_view(), name="things"),
    path('<int:pk>/',ThingDetailsView.as_view(), name="thing_detail")
]