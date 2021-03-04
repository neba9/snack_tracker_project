from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import snacks

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = snacks

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = snacks

# Create your views here.
