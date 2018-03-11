from django.contrib import admin
from .models import Employee, IdentityDocument, Dependents

# Register your models here.
admin.site.register(Employee)
admin.site.register(IdentityDocument)
admin.site.register(Dependents)