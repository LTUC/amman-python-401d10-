from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, ThingsListView, ThingDetailsView, ThingCreateView, ThingUpdateView, ThingDeleteView

urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('things',ThingsListView.as_view(), name="things"),
    path('<int:pk>/',ThingDetailsView.as_view(), name="thing_detail"),
    path('create/',ThingCreateView.as_view(), name="thing_create"),
    path('update/<int:pk>',ThingUpdateView.as_view(), name="thing_update"),
    path('delete/<int:pk>',ThingDeleteView.as_view(), name="thing_delete"),
]