from django.urls import path
from .views import HomePageView, RezeptListView, RezeptDetailView, RezeptNeuView
# from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('liste/', RezeptListView.as_view(), name='list'),
 #   path('liste/', views.liste, name='list'),
    path('rezept/<int:pk>/', RezeptDetailView.as_view(), name='redetail'),
    path('reneu/', RezeptNeuView.as_view(), name='reneu'),
]