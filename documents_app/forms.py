from django import forms
from .models import TimeSheet, Constants


class TimeSheetForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        exclude = ['worktime']


class ConstantsForm(forms.ModelForm):
    class Meta:
        model = Constants
        exclude = ['coding_constant_name']