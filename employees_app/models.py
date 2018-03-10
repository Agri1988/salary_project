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
        return ('%s %s %s' %(self.document_name, self.document_serial, self.document_number))


class Employee(models.Model):
    second_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Фамилия')
    first_name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Имя')
    patronymic = models.CharField(max_length=32, blank=False, null=False, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения')
    identity_document = models.OneToOneField('IdentityDocument', on_delete=models.CASCADE, blank=False, null=False,
                                          verbose_name='Пасспортные данные')
    address = models.CharField(max_length=256, blank=False, null=False, verbose_name='Адрес')
    date_of_employment = models.DateField(verbose_name='Дата приема на работу')
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения', blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['second_name', 'first_name', 'patronymic']

    def __str__(self):
        return ('%s %s %s' %(self.second_name, self.first_name, self.patronymic))

