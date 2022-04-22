from django.urls import path
from . import views
urlpatterns = [
    path('', views.contact, name='contact'),

    # rest app
    path('contact_api', views.Contact_api.as_view(), name='contact_api')
]

