from django.urls import path
from . import views
urlpatterns = [
    path('', views.contact, name='contact'),

    # rest app
<<<<<<< HEAD
    path('contact_api', views.Contact_api.as_view(), name='contact_api')
=======
    # path('', views.Contact_api.as_view(), name='contact')
>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83
]

