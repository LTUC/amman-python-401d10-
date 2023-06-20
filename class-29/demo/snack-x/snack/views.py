from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = "snack/snack-list.html"
    model = Snack


class SnackDetailView(DetailView):
    template_name = "snack/snack-detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack/snack-create.html"
    model = Snack
    fields = ['name','purchaser','desc']


class SnackUpdateView(UpdateView):
    template_name = "snack/snack-update.html"
    model = Snack
    fields = ['name','purchaser','desc']


class SnackDeleteView(DeleteView):
    template_name = "snack/snack-delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")