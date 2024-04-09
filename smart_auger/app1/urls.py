from django.urls import path

from . import views
from .views import UpdateData,TaskDeleteView,DataManageAPIView,TaskDeleteView1,LoginAPIView

urlpatterns = [

path('',views.user_login,name='login'),
path('logout/', views.user_logout, name='logout'),
path('login_api/', LoginAPIView.as_view(), name='api-login'),  
path('home/',views.home,name='home'),
path('map/',views.map_interface,name='map'),
path('user_management/',views.user_management,name='user_management'),
path('add_user/',views.add_user,name='add_user'),
path('delete1/<int:pk>/', TaskDeleteView1.as_view(), name='task_delete1'),
path('reports/',views.reports,name='reports'), 
path('data_management/',views.data_management_view,name='data_management'),
path('add_reco/',views.add_reco,name='add_reco'),
path('update/<int:pk>/', UpdateData.as_view(), name='user_update'),
path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
path('alert_configurationt/',views.alert_configuration,name='alert_configuration'),
path('activitylogs/',views.activitylogs,name='activitylogs'),
path('access_control/',views.access_control,name='access_control'),
path('recorded_zone/',views.recorded_zone,name='recorded_zone'),
path('reports_and_analytics/',views.reports_and_analytics,name='reports_and_analytics'),
path('extra/',views.extra,name='extra'),
path('data_manage_api/',DataManageAPIView.as_view(),name='data_manage_api'),
path('extra1/',views.get_extra,name='extra1'),
]

