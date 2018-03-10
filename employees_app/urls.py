from django.urls import path, include
from . import views, forms

app_name = 'employees_app'
urlpatterns = [
    path('', views.all_employees, name='all_employees'),
    path('<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('add_identity_document/', views.add_identity_document, {'form':forms.IdentityDocumentForm,
                                              'template':'employees_app/add_identity_document.html',
                                              'fieldname': ['document_name', 'document_serial','document_number']},
                                                name='add_identity_document'),

]
