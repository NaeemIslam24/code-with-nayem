from django.shortcuts import render, redirect
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from pricing.models import Purchasing
from . forms import ProfileForm
<<<<<<< HEAD
=======
from django.core.mail import send_mail
from django.conf import settings


>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83
# for rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
<<<<<<< HEAD
# from . serializers import Profile_serializer

class Account_api(APIView):
    def post(self, request, *args,**kwargs):
        if request.method == 'POST':
            username=request.data['user_name']
            email=request.data['email']
            password=request.data['password']
            confirm_password=request.data['confirm_password']

            if User.objects.filter(username=username).exists():
                return Response({"error": "An user already exists with this username!"})

            if password != confirm_password:
                return Response({"error": " Password and Confirm Password not matched!"})

            user = User()
            user.username = username
            user.email = email
            user.password = password
            user.is_active = True
            user.set_password(raw_password=password) # this is valid hash password
            user.save()
            return Response({"success": "An user successfully creates an account"})
=======
from . serializers import Profile_serializer

# class Account_api(APIView):
#     def post(self, request, *args,**kwargs):
#         if request.method == 'POST':
#             username=request.data['user_name']
#             email=request.data['email']
#             password=request.data['password']
#             confirm_password=request.data['confirm_password']
#
#             if User.objects.filter(username=username).exists():
#                 return Response({"error": "An user already exists with this username!"})
#
#             if password != confirm_password:
#                 return Response({"error": " Password and Confirm Password not matched!"})
#
#             user = User()
#             user.username = username
#             user.email = email
#             user.password = password
#             user.is_active = True
#             user.set_password(raw_password=password) # this is valid hash password
#             user.save()
#             return Response({"success": "An user successfully creates an account"})
>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83


def account(request):

    if request.method == 'POST':
        name = request.POST.get('name') #same as  name = request.POST['name']
        uname = request.POST.get('user_name')
        email = request.POST.get('email')
        psd = request.POST.get('password')
        cpsd = request.POST.get('confirm_password')
        if psd == cpsd:
            if User.objects.filter(username=uname).exists():

                messages.error(request, 'Username already exists!')
                return redirect('account')

            elif User.objects.filter(email=email).exists():

                messages.error(request, 'The Email already exists!')
                return redirect('account')

            else:

                user = User.objects.create_user(
                    username=uname, email=email, password=psd, first_name=name)

                user.save()
                profile = Profile.objects.filter(user=user).first()
                token = profile.auth_token
                sent_registation_mail(email, token, uname)
                return redirect('verify')

        else:
            messages.error(request, 'Password and confirm-password not matched!')
            return redirect('account')

    template = 'account/account.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }

    return render(request, template_name=template, context=context)

class Login_api(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
      
        if user is not None:
            login(request, user)
            return Response({"success":"Login successful"})
        else:
            return Response({"error":"username or password invalid"})


def verify(request):
    template = 'account/verify.html'
    if request.method == 'POST':
        code = request.POST.get('code')
        profile = Profile.objects.filter(auth_token=code).first()
        if profile:
            if profile.is_verified:
                messages.success(request, 'Your account already verified')
                return redirect('login')
            profile.is_verified = True
            profile.save()
            messages.success(request, 'Your account is verified')
            return redirect('login')
        else:
            messages.error(request, 'Not matched the code check your email')







    return render(request, template_name=template)

# class Login_api(APIView):
#     def post(self,request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return Response({"success":"Login successful"})
#         else:
#             return Response({"error":"username or password invalid"})


def authlogin(request):
    template = 'account/login.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,

    }

    if request.method == 'POST':
        uname = request.POST.get('name')
        psd = request.POST.get('password')
        user = authenticate(request, username=uname, password=psd)
        profile = Profile.objects.filter(user=user).first()
        try:
            if not profile.is_verified:
                messages.error(request, 'Your account not verified check your mail')
                return redirect('login')
            if profile is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Invalid password or username')

        except Exception:
            messages.error(request, 'No profile for Superuser')
            return  redirect('login')

    return render(request, template_name=template, context=context)


def forget(request):
    template = 'account/forget.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }
    return render(request, template_name=template, context=context)
from django.forms.models import model_to_dict
import json

# class Profile_api(APIView):
#     def get(self,request,*args, **kwargs):
#
#         data = request.user.profile
#
#
#         return Response(data.data)

# class Profile_api(APIView):
#     def get(self,request,*args, **kwargs):
#
#         data = request.user.profile
#
#         serialized = Profile_serializer(data, many=True)
#         return Response(serialized.data)

# class Service_api(APIView):
#     def get(self,request,*args, **kwargs):
#         service = Service.objects.all()

#         service_serializer = Service_serializer(service, many=True)

 

#         return Response(service_serializer.data)

def profile(request):
    template = 'account/profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
<<<<<<< HEAD
    profile = request.user.profile #to have corrent user "request.user"

    
    pro = False
    if profile.active_pro:
        purchase = request.user.profile.purchasing 
        pro = True
        context = {
           'top_headerdata': top_header,
           'headerdata': header,
           'footer1': top_footer1,
           'footer2': top_footer2,
           'footer3': top_footer3,
           'footer4': top_footer4,
           'profile': profile,
           'pro': pro,
           'purchase': purchase,
       }
    else:
=======
    try:
        profile = request.user.profile




        context = {
            'top_headerdata': top_header,
            'headerdata': header,
            'footer1': top_footer1,
            'footer2': top_footer2,
            'footer3': top_footer3,
            'footer4': top_footer4,
            'profile': profile,
        }
    except Exception:
        messages.error(request, 'No profile for Superuser')
        return redirect('login')

>>>>>>> 5da3233635c387b653becb86a2c5da50ae42bf83

       context = {
           'top_headerdata': top_header,
           'headerdata': header,
           'footer1': top_footer1,
           'footer2': top_footer2,
           'footer3': top_footer3,
           'footer4': top_footer4,
           'profile': profile,
           'pro': pro,
       }
    return render(request, template_name=template, context=context)


def update_profile(request):

    template = 'account/update_profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()

    if request.method == "POST":
        profile = request.user.profile
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        pform.save()
        return redirect('profile')
    else:
        # here user father and profile is son it happens when user is used with OneToOneFiedls
        profile = request.user.profile

        pform = ProfileForm(instance=profile)

    context = {
        'form': pform,
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }
    return render(request, template_name=template, context=context)


def userlogout(request):
    logout(request)
    return redirect('login')


def sent_registation_mail(email, token, username):
    subject = 'Your accounts need to be verified'
    message = f'Hi {username}! welcome to Stack Pro. Here is the verification CODE  {token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)