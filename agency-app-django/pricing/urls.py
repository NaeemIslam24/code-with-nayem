from django.urls import path
from . import views
urlpatterns = [
    path('', views.pricing, name='pricing'),
    path('purchasing', views.purchasing, name='purchasing'),
    path('wait', views.wait, name='wait'),
]