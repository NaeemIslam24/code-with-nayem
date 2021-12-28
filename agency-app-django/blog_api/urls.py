from django.urls import path
from . import views


urlpatterns = [
    path('', views.Post_api.as_view(), name='blogApi'),
    path('<int:pk>/', views.Post_detail.as_view(), name='blogDetail'),

]
