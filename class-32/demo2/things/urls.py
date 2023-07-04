from django.urls import path
from .views import ThingsList, ThingDetail

urlpatterns = [
    path('', ThingsList.as_view(), name='things_list'),
    path('<int:pk>/', ThingDetail.as_view(), name='thing_detail'),
]
