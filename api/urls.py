from django.urls import path
from . import views

urlpatterns = [
    path('api/resource/', views.ResourceListCreate.as_view() ),
]