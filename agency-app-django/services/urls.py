from django.urls import path
from . import views
urlpatterns = [
    path('', views.services, name='services'),
    path('service-api/', views.Service_api.as_view(), name='service_api')
]