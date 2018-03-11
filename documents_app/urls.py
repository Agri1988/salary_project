from django.urls import path, include
from . import views, forms

app_name = 'documents_app'
urlpatterns = [
    path('timesheets/', views.all_timesheets, name='all_timesheets'),
    path('timesheets/<str:timesheet_date>/', views.timesheet_detail, name='timesheet_detail'),

    path('new_timesheet/', views.timesheet_detail, name='timesheet_new'),
    path('save_timesheet/', views.save_timesheet, name='save_timesheet'),

    path('constants/', views.all_constants, name='all_constants'),
    path('constants/<int:constant_id>/', views.constant_detail, name='constant_detail'),

]