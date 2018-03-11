from django.shortcuts import render
from .forms import TimeSheetForm, ConstantsForm
from .models import TimeSheet, Constants
from  employees_app.models import Employee
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template.loader import get_template
import calendar
import datetime
from public_functions.PublicFunction import get_days_list
# Create your views here.

def all_timesheets(request):
    timesheets = TimeSheet.objects.all()
    timesheets_date = []
    for timesheet in timesheets:
        if timesheet.date not in timesheets_date:
            timesheets_date.append(timesheet.date)
    context = {'timesheets':timesheets_date}
    return render(request, 'documents_app/all_timesheets.html', context)


def timesheet_detail(request, timesheet_date=None):
    print(request.POST)
    if timesheet_date != None:
        timesheets = TimeSheet.objects.filter(date=timesheet_date)
        if len(timesheets) != 0:
            timesheets = [[timesheet.employee, timesheet.date,[el for el in timesheet.worktime.split(';')], \
                           timesheet.workhours_in_month, timesheet.workdays_in_month,
                           timesheet.norm_days_hours_in_month.split('/')[0],
                           timesheet.norm_days_hours_in_month.split('/')[1]] for timesheet in timesheets]
            print(timesheets)
    else:
        timesheets = None
    employees = Employee.objects.filter(date_of_dismissal__isnull=True)
    context = {'employees': employees, 'timesheets': timesheets, 'timesheet_date':timesheet_date}
    if request.POST.get('new'):
        template = get_template('documents_app/new_timesheet.html')
        context.update({'new': True})
        days_list = get_days_list(int(timesheet_date[5:7]), int(timesheet_date[:4]))
        workdays_in_month = len(days_list)- days_list.count('В')
        workhours_in_month = workdays_in_month*8
        context.update({'days_list':days_list})
        context.update({'workhours_in_month':workhours_in_month})
        context.update({'workdays_in_month': workdays_in_month})
        return HttpResponse(template.render(context, request))
    return render(request, 'documents_app/detail_timesheet.html', context)


def save_timesheet(request):
    def serialize_data_to_db(lst, employee_count):
        lst = lst.split('&')
        # lst = [i.decode('utf8') for i in lst]
        count_element = int(len(lst) / employee_count)
        new_lst = []
        for i in range(2):
            new_lst.append(lst[:count_element])
            lst = lst[count_element:]
        dict_ = {}
        for el in new_lst:
            for el2 in el:
                if ('employee' in el2) and (el2[9:] not in dict_.keys()):
                    dict_[el2[9:]] = [x.split('=')[1] for x in el[1:]]
        return (dict_)
    serialize_data = serialize_data_to_db(request.POST['serialize_data'], int(request.POST['line_count']))
    print(request.POST)
    date = request.POST['date']
    date = datetime.date(int(date[:4]), int(date[5:7]), 1)
    timesheets = TimeSheet.objects.filter(employee__in=serialize_data.keys()).filter(date=date)
    if (len(timesheets)==0):
        for key, value in serialize_data.items():
            new_timesheet = TimeSheet()
            new_timesheet.date = date
            new_timesheet.employee = Employee.objects.get(id=int(key))
            new_timesheet.worktime = ';'.join(value[:-2])
            new_timesheet.workdays_in_month = str(value[-1])
            new_timesheet.workhours_in_month = str(value[-2])
            new_timesheet.norm_days_hours_in_month = '%s/%s' %(request.POST['workdays_in_month'],
                                                               request.POST['workhours_in_month'])
            new_timesheet.save()
    else:
        for timesheet in timesheets:
            timesheet.worktime = ';'.join(serialize_data[str(timesheet.employee.pk)][:-2])
            timesheet.workdays_in_month = serialize_data[str(timesheet.employee.pk)][-1]
            timesheet.workhours_in_month = serialize_data[str(timesheet.employee.pk)][-2]
            timesheet.norm_days_hours_in_month = '%s/%s' %(request.POST['workdays_in_month'],
                                                               request.POST['workhours_in_month'])
            timesheet.save()


def all_constants(request):
    constants = Constants.objects.all()
    context = {'constants':constants}
    return render(request, 'documents_app/constants.html', context)


def constant_detail(request, constant_id):
    constant = Constants.objects.get(id=constant_id)
    if request.method != 'POST':
        form = ConstantsForm(instance=constant)
    else:
        form = ConstantsForm(instance=constant, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('documents_app:constant_detail', args=[constant_id]))
    context = {'form':form, 'constant_id':constant_id}
    return render(request, 'documents_app/constant_detail.html', context)


def all_payroll(request):
    pass