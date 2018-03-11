from django.db import models


class IdentityDocument(models.Model):
    document_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Наименование документа')
    document_serial = models.CharField(max_length=32, blank=False, null=False, verbose_name='Серия документа')
    document_number = models.CharField(max_length=32, blank=False, null=False, verbose_name='Номер документа')
    personal_number = models.CharField(max_length=32, blank=False, null=False, verbose_name='Личный номер')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    date_of_validity = models.DateField(verbose_name='Действителен до')
    issuing_authority = models.CharField(max_length=256, blank=False, null=False, verbose_name='Орган выдавший документ')

    class Meta:
        verbose_name = 'Документ удостоверяющий личность'
        verbose_name_plural = 'Документы удостоверяющие личность'

    def __str__(self):
        return ('%s %s %s'%(self.document_name, self.document_serial, self.document_number))


class Dependents(models.Model):
    employee = models.OneToOneField('Employee', on_delete=models.CASCADE, verbose_name='Сотрудник')
    child_under_18 = models.IntegerField(blank=False, null=False, verbose_name='Дети до 18 лет', default=0)
    disabled_child_under_18 = models.IntegerField(blank=False, null=False, verbose_name='Дети-инвалиды до 18 лет', default=0)
    spouse_on_maternity_leave = models.BooleanField(verbose_name='Супруг/супруга в отпуске по уходу за ребенком', default=False)
    child_after_18 = models.IntegerField(blank=False, null=False, verbose_name='Обучающиеся дети старше 18 лет', default=0)
    legal_guardian_status = models.BooleanField(verbose_name='Является одиноким родителем/приемным родителем/ пекуном/\
                                                попечителем', default=False)

    class Meta:
        verbose_name = 'Иждивенцы'
        verbose_name_plural = 'Иждивенцы'

    def __str__(self):
        return '%s %s %s - иждивенцы'%(self.employee.second_name, self.employee.first_name, self.employee.patronymic)


class Employee(models.Model):
    CHOICE_EMPLOYEEMENT_TYPE = [('1', 'Основное'), ('1', 'Совместительство'), ('1', 'Договор подряда')]
    second_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=32, blank=False, null=False, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    identity_document = models.OneToOneField('IdentityDocument', on_delete=models.CASCADE, blank=False, null=False,
                                          verbose_name='Пасспортные данные')
    address = models.CharField(max_length=256, blank=False, null=False, verbose_name='Адрес')
    position = models.CharField(max_length=128, blank=False, null=False, verbose_name='Должность')
    employeement_type = models.CharField(max_length=16, blank=False, null=False, verbose_name='Тип трудоустройства',
                                         choices=CHOICE_EMPLOYEEMENT_TYPE)
    tariff_salary = models.DecimalField(verbose_name='Тарифная ставка', decimal_places=2, max_digits=99)
    date_of_employment = models.DateField(verbose_name='Дата приема на работу')
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['second_name', 'first_name', 'patronymic']

    def __str__(self):
        return ('%s %s %s' %(self.second_name, self.first_name, self.patronymic))

