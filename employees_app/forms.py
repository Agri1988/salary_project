from django import forms
from .models import Employee, IdentityDocument


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class IdentityDocumentForm(forms.ModelForm):
    class Meta:
        model = IdentityDocument
        fields = '__all__'