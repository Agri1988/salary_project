from django import forms
from .models import TimeSheet


class TimeSheetForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        exclude = ['worktime']