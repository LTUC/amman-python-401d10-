from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Thing
from django.urls import reverse_lazy

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

class ThingCreateView(CreateView):
    template_name='thing_create.html'
    model=Thing
    fields= ['name', 'rating', 'desc', 'reviewer']

class ThingUpdateView(UpdateView):
    template_name='thing_update.html'
    model=Thing
    fields="__all__"
    success_url=reverse_lazy('things')

class ThingDeleteView(DeleteView):
    template_name='thing_delete.html'
    model=Thing
    success_url=reverse_lazy('things')

