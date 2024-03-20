from django.shortcuts import render

def home(request):
    return render(request,'app1/home.html')

def map_interface(request):
    return render(request,'app1/map_interface.html')

def user_management(request):
    return render(request,'app1/user_management.html')

def reports(request):
    return render(request,'app1/reports.html')

def data_management(request):
    return render(request,'app1/data_management.html')

def alert_configuration(request):
    return render(request,'app1/alert_configuration.html')

def activitylogs(request):
    return render(request,'app1/activitylogs.html')

def access_control(request):
    return render(request,'app1/access_control.html')

def recorded_zone(request):
    return render(request,'app1/recorded_zone.html')

def reports_and_analytics(request):
    return render(request,'app1/reports_and_analytics.html')

def extra(request):
    return render(request,'app1/extra.html')