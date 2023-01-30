from django.urls import path
from . import views
app_name='employee'

urlpatterns=[
  path('leave',views.leave,name='hrleave'),
  path('calender',views.calender, name='hrcalender'),
  path('dashboard',views.dashboard, name='hrdashboard'),
  path('master',views.master),
  path('hrlogin',views.hrlogin, name='hrlogin'),
  path('attendence',views.attendence, name='hrattendence'),
  path('newpage',views.newpage),
]