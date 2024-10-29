from django.urls import path
from .views import BarberListView, BarberDetailView, BarberCreateView, BarberUpdateView, CBListView
from . import views

urlpatterns = [
    path('', BarberListView.as_view(), name='b_list'),
    path('<int:pk>/', BarberDetailView.as_view(), name='b_detail'),
    path('new/', BarberCreateView.as_view(), name='b_new'),
    path('<int:pk>/edit/', BarberUpdateView.as_view(), name='b_edit'),
    path('cblist/', CBListView.as_view(), name='cb_list'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
]