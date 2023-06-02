from django.contrib import admin
from customer.models import *
# Register your models here.

admin.site.register(customers)

admin.site.register(CustomerAddress)
admin.site.register(CustomerAadhar)