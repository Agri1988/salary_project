from django.db import models
from employees_app.models import Employee


# Create your models here.
class TimeSheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Сотрудник')
    date = models.DateField(verbose_name='Дата')
    worktime = models.CharField(max_length=128, blank=False, null=False, verbose_name='Отработанное время')

    class Meta:
        verbose_name = 'График отработанного времени'
        verbose_name_plural = "Графики отработанного времени"
        ordering = ['date']