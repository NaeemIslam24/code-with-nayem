from django.urls import path
from . import views
urlpatterns = [
    path('', views.team, name='team'),


        #API path
    path('team_api',views.Team_api.as_view(),name='team_api' ),

]