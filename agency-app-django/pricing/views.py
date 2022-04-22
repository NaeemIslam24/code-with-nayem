from django.shortcuts import render, redirect
from header.models import Top_header, Header
from footer.models import Top_footer1, Top_footer2, Top_footer4, Top_footer3
from .forms import Purchasing_model
from .models import Purchasing
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)

def pricing(request):
    template = 'pricing.html'
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



def purchasing(request):
    template = 'purchasing.html'
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_footer1 = Top_footer1.objects.order_by()
    top_footer2 = Top_footer2.objects.order_by()
    top_footer3 = Top_footer3.objects.order_by()
    top_footer4 = Top_footer4.objects.order_by()

    purchasing_form = Purchasing_model()

    user_active = Purchasing.objects.filter(active = True)


    if user_active:

        redirect('account')



   
    if request.method == 'POST':

        post_form = Purchasing_model(request.POST)

        if post_form.is_valid():
           
           post_form.save()
        
        return redirect('wait')

    context = {
        'hello': purchasing_form,
        'top_headerdata': top_header,
        'headerdata': header,
        'footer1': top_footer1,
        'footer2': top_footer2,
        'footer3': top_footer3,
        'footer4': top_footer4,
    }

    return render(request, template_name=template, context=context)

def wait(request):
    template = 'wait.html'
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
