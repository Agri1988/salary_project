from django.contrib import admin
from .models import Employee, IdentityDocument

# Register your models here.
admin.site.register(Employee)
admin.site.register(IdentityDocument)