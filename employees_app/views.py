from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.http import JsonResponse
from django.urls import reverse
from .models import Employee
from .forms import EmployeeForm, IdentityDocumentForm


# Create your views here.
def all_employees(request):
    employees = Employee.objects.all()
    context = {'employees':employees}
    return render(request, 'employees_app/all_employees.html', context)


def employee_detail(request, employee_id):
    if employee_id == 0:
        employee = None
    else:
        employee = Employee.objects.get(pk=employee_id)

    if request.method != 'POST':
        employee_form = EmployeeForm(instance=employee, initial=None)
    else:
        employee_form = EmployeeForm(instance=employee, data=request.POST)
        if employee_form.is_valid():
            new_employee = employee_form.save()
            employee_id = new_employee.id
            return HttpResponseRedirect(reverse('employees_app:employee_detail', args=[employee_id]))
    context = {'employee_form':employee_form, 'employee_id':employee_id}
    return render(request, 'employees_app/employee_detail.html', context)


def add_identity_document(request, template, form, fieldname):
    if request.method != 'POST':
        context = {'form': form()}
        template = get_template(template)
        return HttpResponse(template.render(context, request))
    else:
        print(request.POST)
        form = form(data=request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            new_element = form.save()
            new_element_id = new_element.id
            new_element_name = str(getattr(new_element, fieldname[0]))+' '+str(getattr(new_element, fieldname[1]))+' '+\
                                str(getattr(new_element, fieldname[2]))
        data_dict = {'new_element_id':new_element_id, 'new_element_name':new_element_name}
        return JsonResponse(data_dict)
