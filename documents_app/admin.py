from django.contrib import admin
from .models import TimeSheet, Constants, Payroll

admin.site.register(TimeSheet)
admin.site.register(Constants)
admin.site.register(Payroll)

# Register your models here.
