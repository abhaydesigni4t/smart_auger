from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import data_management_model,user_management_model,Location
from .forms import user_management_form1,LoginForm,LocationForm
from .serializers import DataManageSerializer,LoginSerializer
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import json


def home(request):
    return render(request,'app1/home.html')

def map_interface(request):
    # Query the database to get all recordings
    recordings = data_management_model.objects.all()
    
    # Construct locations data with latitude and longitude as floats
    locations_data = [{
        'lat': recording.latitude,
        'lng': recording.longitude,
        'name': f"Recording {recording.rec_no}"
    } for recording in recordings]

    # Pass locations_data to the template
    return render(request, 'app1/map_interface.html', {'locations_data': locations_data})

def user_management(request):
    data = user_management_model.objects.all()
    return render(request,'app1/user_management.html',{'data':data})

def add_user(request):
    if request.method == 'POST':
        form = user_management_form1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = user_management_form1()  
    return render(request, 'app1/add_user.html', {'form': form})


class TaskDeleteView1(DeleteView):
    model = user_management_model
    template_name = 'app1/data_confirm_delete1.html'
    success_url = reverse_lazy('user_management')

def reports(request):
    return render(request,'app1/reports.html')


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

def data_management_view(request):
    recordings = Location.objects.all()
    return render(request, 'app1/data_management.html', {'recordings': recordings})


def add_reco(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_management')
    else:
        form = LocationForm()
    return render(request, 'app1/add_record.html', {'form': form})


class UpdateData(UpdateView):
    model = Location
    fields = '__all__'     
    template_name = 'app1/add_record.html'
    success_url = reverse_lazy('data_management')

class TaskDeleteView(DeleteView):
    model = Location
    template_name = 'app1/data_confirm_delete.html'
    success_url = reverse_lazy('data_management')


class DataManageAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = DataManageSerializer

    def post(self, request, *args, **kwargs):
        # Exclude 'timestamp' field from data when creating a new record
        request_data_without_timestamp = request.data.copy()
        request_data_without_timestamp.pop('timestamp', None)
        
        serializer = DataManageSerializer(data=request_data_without_timestamp)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
            else:             
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'app1/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
           
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def map_view(request):
    locations = Location.objects.all()
    locations_data = [{'lat': location.latitude, 'lng': location.longitude} for location in locations]
    return render(request, 'app1/gmap.html', {'locations_data': json.dumps(locations_data)})

def delete_selected(request):
    if request.method == 'POST':
        selected_recordings = request.POST.getlist('selected_recordings')
        if 'select_all' in request.POST:  
            selected_recordings = [str(recording.pk) for recording in Location.objects.all()]
        Location.objects.filter(pk__in=selected_recordings).delete()
        return redirect('data_management')  
    return redirect('data_management')  


def delete_selected1(request):
    if request.method == 'POST':
        selected_records = request.POST.getlist('selected_recordings')
        if 'select_all' in request.POST:
            selected_records = [str(record.pk) for record in user_management_model.objects.all()]
        user_management_model.objects.filter(pk__in=selected_records).delete()
        return redirect('user_management')  
    return redirect('user_management')


class LocationListAPI(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = DataManageSerializer(locations, many=True)
        data = {
            'count': locations.count(),
            'data': serializer.data
        }
        return Response(data)


class DataAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return Response(data, status=200)
