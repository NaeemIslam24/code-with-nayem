from django.urls import path
from . import views
# pass reset
from django.contrib.auth import views as auth_view
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns = [


    path('', views.account, name='account'),
    path('login/', views.authlogin, name='login'),
    path('verify/', views.verify, name='verify'),
    path('profile/', views.profile, name='profile'),
    path('forget/', views.forget, name='forget'),
    path('logout/', views.userlogout, name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
    # password reset start
    path('reset_pass/', auth_view.PasswordResetView.as_view(
        template_name='account/password_reset.html'), name="reset_password"),
    path('reset_pass_sent/', auth_view.PasswordResetDoneView.as_view(template_name='account/password_reset_sent.html'),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='account/reset.html'),
         name="password_reset_confirm"),
    path('reset_pass_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='account/reset_complete.html'),
         name="password_reset_complete"),
    # password reset send


<<<<<<< HEAD
    #API path
    path('account_api',views.Account_api.as_view(),),
    path('login_api/',views.Login_api.as_view(),),
    # path('profile_api/', views.Profile_api.as_view(), ),

    #authentiation
=======
    # #API path
    # path('',views.Account_api.as_view(), name='account'),
    # path('login/',views.Login_api.as_view(), name='login'),
    # # path('profile/', views.Profile_api.as_view(), name='profile'),
    #
    # #authentiation
>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83
    # path('api-token/',obtain_auth_token),
]
