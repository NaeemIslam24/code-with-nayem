from django.shortcuts import render, redirect
from .models import *
from header.models import *
from footer.models import *


def contact(request):
    submitted = False
    template = 'contact.html'

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_data = Contact(name=name, email=email, subject=subject, message=message)
        contact_data.save()
        return redirect('/contact?submitted')

    else:
        if 'submitted' in request.GET:
            submitted = True
    top_header = Top_header.objects.order_by()
    header = Header.objects.order_by()
    top_contact = Top_contact.objects.order_by()
    top_contact2 = Top_contact2.objects.order_by()
    top_contact3 = Top_contact3.objects.order_by()
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
        'top_contactdata': top_contact,
        'top_contactdata2': top_contact2,
        'top_contactdata3': top_contact3,
        'submitted': submitted,
    }

    return render(request, template_name=template, context=context)
