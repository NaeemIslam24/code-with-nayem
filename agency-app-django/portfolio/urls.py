from django.urls import path
from . import views
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('details/<int:pk>/<str:title>/', views.details, name='details'),
]
