from django.contrib import admin
from .models import User, Company, Customer
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Company)