from django.urls import path
from . import views


urlpatterns = [
    path('', views.Post_api.as_view(), name='list',),
    path('retrive-update/<str:pk>/', views.Retrive_update.as_view(), name="nayem",),

]


