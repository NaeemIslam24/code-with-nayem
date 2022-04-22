from django import forms
from .models import Purchasing


class Purchasing_model(forms.ModelForm):

    class Meta:
        model = Purchasing
        # exclude = ['active','requested_time','name']
        # fields = '__all__'
        fields = ("plan_name","profi", "banking_name","transaction_id", "number", "How_much_you_paid")