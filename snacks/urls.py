from snacks.models import snacks
from django.urls import path, include
from .views import SnackListView, SnackDetailView

urlpatterns = [
  path('', SnackListView.as_view(), name='snacks_list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snacks_detail'),
]