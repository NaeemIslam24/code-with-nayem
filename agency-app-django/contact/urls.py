from django.urls import path
from . import views
urlpatterns = [
    # path('', views.contact, name='contact'),

    # rest app
    path('', views.Contact_api.as_view(), name='contact')
]

