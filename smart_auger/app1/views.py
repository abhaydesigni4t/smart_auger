from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import data_management_model,user_management_model
from .forms import data_management_form,user_management_form,LoginForm
from .serializers import DataManageSerializer,LoginSerializer
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


def home(request):
    return render(request,'app1/home.html')

def map_interface(request):
    return render(request,'app1/map_interface.html')

def user_management(request):
    data = user_management_model.objects.all()
    return render(request,'app1/user_management.html',{'data':data})

def add_user(request):
    if request.method == 'POST':
        form = user_management_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = user_management_form()  
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
    recordings = data_management_model.objects.all()
    return render(request, 'app1/data_management.html', {'recordings': recordings})

def add_reco(request):
    if request.method == 'POST':
        form = data_management_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_management')
    else:
        form = data_management_form()
    return render(request, 'app1/add_record.html', {'form': form})

class UpdateData(UpdateView):
    model = data_management_model
    fields = '__all__'     
    template_name = 'app1/add_record.html'
    success_url = reverse_lazy('data_management')

class TaskDeleteView(DeleteView):
    model = data_management_model
    template_name = 'app1/data_confirm_delete.html'
    success_url = reverse_lazy('data_management')


class DataManageAPIView(generics.ListCreateAPIView):
    queryset = data_management_model.objects.all()
    serializer_class = DataManageSerializer

    def post(self, request, *args, **kwargs):
        serializer = DataManageSerializer(data=request.data)
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
    
def get_extra(request):
    return render(request,'app1/extra2.html')