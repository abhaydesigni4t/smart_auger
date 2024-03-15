from django.urls import path

from . import views


urlpatterns = [
    
path('',views.home,name='home'),
path('map/',views.map_interface,name='map'),
path('user_management/',views.user_management,name='user_management'),
path('reports/',views.reports,name='reports'), 
path('data_management/',views.data_management,name='data_management'),
path('alert_configurationt/',views.alert_configuration,name='alert_configuration'),
path('activitylogs/',views.activitylogs,name='activitylogs'),
]

