from django.contrib import admin
from . models import Purchasing, Plan_category, Banking_name
# Register your models here.

admin.site.register(Plan_category)
admin.site.register(Purchasing)
admin.site.register(Banking_name)