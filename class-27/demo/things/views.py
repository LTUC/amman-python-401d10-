from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Thing

# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class ThingsListView(ListView):
    template_name="things.html"
    model=Thing
    context_object_name = "things"

class ThingDetailsView(DetailView):
    template_name="thing_details.html"
    model=Thing

