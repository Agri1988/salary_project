from django.db import models
from employees_app.models import Employee

class Constants(models.Model):
    coding_constant_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Наименование \
                                            константы для кода')
    constant_name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Наименование константы')
    constant_value = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False, verbose_name='Значение константы')

    class Meta:
        verbose_name = 'Константа'
        verbose_name_plural = 'Константы'

    def __str__(self):
        return '%s: %s'%(self.constant_name, self.constant_value)


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


class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Сотрудник')
    date = models.DateField(verbose_name='Дата начислений')
    payrolls = models.CharField(max_length=512, blank=False, null=False, verbose_name='Начисления')
    deductions = models.CharField(max_length=512, blank=False, null=False, verbose_name='Удержания')
    accruals_summ = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False,
                                        verbose_name='Сумма начислений')
    deductions_summ = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False,
                                        verbose_name='Сумма удержаний')
    result = models.DecimalField(decimal_places=2, max_digits=20, blank=False, null=False,
                                        verbose_name='Итого')
    class Meta:
        verbose_name = 'Начисление заработной платы'
        verbose_name_plural = "Начисления заработной платы"

    def __str__(self):
        return '%s %s.%s'%(self.employee, self.date._month, self.date._year)
