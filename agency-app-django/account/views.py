from django.shortcuts import render, redirect
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from . forms import ProfileForm
# for rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import Profile_serializer

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


# def account(request):
#
#     if request.method == 'POST':
#         name = request.POST.get('name') #same as  name = request.POST['name']
#         uname = request.POST.get('user_name')
#         email = request.POST.get('email')
#         psd = request.POST.get('password')
#         cpsd = request.POST.get('confirm_password')
#         if psd == cpsd:
#             if User.objects.filter(username=uname).exists():
#
#                 messages.error(request, 'Username already exists!')
#
#             elif User.objects.filter(email=email).exists():
#
#                 messages.error(request, 'The Email already exists!')
#
#             else:
#                 user = User.objects.create_user(
#                     username=uname, email=email, password=psd, first_name=name)
#                 user.save()
#                 return redirect('login')
#
#         else:
#             messages.error(
#                 request, 'Password and confirm-password not matched!')
#
#     template = 'account/account.html'
#     top_header = Top_header.objects.order_by()
#     header = Header.objects.order_by()
#     top_footer1 = Top_footer1.objects.order_by()
#     top_footer2 = Top_footer2.objects.order_by()
#     top_footer3 = Top_footer3.objects.order_by()
#     top_footer4 = Top_footer4.objects.order_by()
#     context = {
#         'top_headerdata': top_header,
#         'headerdata': header,
#         'footer1': top_footer1,
#         'footer2': top_footer2,
#         'footer3': top_footer3,
#         'footer4': top_footer4,
#     }
#
#     return render(request, template_name=template, context=context)

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


# def authlogin(request):
#     template = 'account/login.html'
#     top_header = Top_header.objects.order_by()
#     header = Header.objects.order_by()
#     top_footer1 = Top_footer1.objects.order_by()
#     top_footer2 = Top_footer2.objects.order_by()
#     top_footer3 = Top_footer3.objects.order_by()
#     top_footer4 = Top_footer4.objects.order_by()
#
#     context = {
#         'top_headerdata': top_header,
#         'headerdata': header,
#         'footer1': top_footer1,
#         'footer2': top_footer2,
#         'footer3': top_footer3,
#         'footer4': top_footer4,
#
#     }
#
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         psd = request.POST.get('password')
#         user = authenticate(request, username=uname, password=psd)
#         if user is not None:
#             login(request, user)
#             return redirect('profile')
#         else:
#             messages.error(request, 'Invalid password or username')
#
#     return render(request, template_name=template, context=context)


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

# class Profile_api(APIView):
#     def get(self,request,*args, **kwargs):
#
#         data = request.user.profile
#
#         serialized = Profile_serializer(data, many=True)
#         return Response(serialized.data)

def profile(request):
    template = 'account/profile.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()
    profile = request.user.profile


    print('-----------------',profile)

    context = {
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
        'profile': profile,
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
