from django.shortcuts import render

# Create your views here.

def leave(request):
    return render(request,'employee/leave.html')

def calender(request):
    return render(request,'employee/calender.html')

def dashboard(request):
    return render(request,'employee/dashboard.html')

def master(request):
    return render(request,'employee/master.html')

def hrlogin(request):
    return render(request,'employee/hrlogin.html')

def attendence(request):
    return render(request,'employee/attendence.html')

def newpage(request):
    return render(request,'employee/newpage.html')