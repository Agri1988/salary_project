from django.db import models
from employees_app.models import Employee


# Create your models here.
class TimeSheet(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Сотрудник')
    date = models.DateField(verbose_name='Дата')
    worktime = models.CharField(max_length=128, blank=False, null=False, verbose_name='Отработанное время')
    workdays_in_month = models.IntegerField(blank=False, null=False, verbose_name='Количество рабочих дней')
    workhours_in_month = models.IntegerField(blank=False, null=False, verbose_name='Количество рабочих часов')
    norm_days_hours_in_month = models.CharField(max_length=8, blank=False, null=False, verbose_name='Норма часов/дней')

    class Meta:
        verbose_name = 'График отработанного времени'
        verbose_name_plural = "Графики отработанного времени"
        ordering = ['date']

    def __str__(self):
        return ('%s %s' %(self.date, self.employee))