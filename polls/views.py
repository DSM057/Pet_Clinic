from functools import total_ordering
from importlib.metadata import requires
import json
import random
import re
import string
from urllib.request import Request
import uuid
from wsgiref.util import request_uri
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Client, TypeAnimal, Booking, ClientAnimal
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers




def index(request, src='#ffffff', h1="Вітаю вас в Ветеренарній клініці VETDIM"):
    link_src = src
    link_h1 = h1
    return render(request, 'index.html', {'link_src' : link_src, 'link_h1' : link_h1})

def first_choise(request):
    return render(request , 'page1.html')

def survey(request, src='#ffffff', h1="Якість наданих полслуг"):
    link_src = src
    link_h1 = h1
    return render(request, 'survey.html', {'link_src' : link_src, 'link_h1' : link_h1})

def last_booking(request):
    bookings = Booking.objects.all()[0:5]
    total_bookings = Booking.objects.count()
    return render(request, 'index.html' , {'bookings':bookings , 'total_bookings':total_bookings})

def load_more(request):
    total_item = int(request.GET.get('total_item'))
    limit = 4
    bookings = list(Booking.objects.values('client__name' , 'date')[total_item:total_item+limit])
    
    for booking in bookings:
        if booking['client__name'] is None:
            booking['client__name'] = "Запис вільний"


    data = {
        'bookings':bookings
        }
    return JsonResponse(data=data)

def last_clients(request):
    all_clients = ClientAnimal.objects.order_by('client')
    return render(request, 'index.html', {'all_clients': all_clients})

def success(request):
    return render(request, 'success.html')

def failed(request):
    return render(request, 'failed.html')

def regiksuccess(request):
    return render(request, 'regiksuccess.html')

def regikfailed(request):
    return render(request, 'regikfailed.html')

def login_failed(request):
    return render(request , 'loginfailed.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request , user)
            return redirect('reg')
        else:
            return redirect('loginfailed')

    return render(request , 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('main')

def regik(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            return redirect('regikfailed')
        
        if form.is_valid():
            form.save()
            return redirect('regiksuccess')

    else:
        form = CreateUserForm()
    
    return render(request, 'regik.html', {'form': form})
           

    return render(request, 'regik.html', {'form': form})

@login_required(login_url='login')
def reg(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        appointment_date = request.POST.get('appointmentDate')
        appointment_time = request.POST.get('appointmentTime')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        pet_type_id = request.POST.get('petType')
        pet_details = request.POST.get('petDetails')

        # Проверяем, существует ли запись о бронировании для выбранной даты и времени
        booking = Booking.objects.filter(date=appointment_date + ' ' + appointment_time,client=None).first()

        if booking:
            # Если запись существует, получаем или создаем клиента
            user, created = User.objects.get_or_create(username=email)
            client, created = Client.objects.get_or_create(user=user,name=name, number=phone, defaults={'surname': surname})
            
            # Обновляем запись о бронировании, добавляя клиента
            booking.client = client
            booking.save()
        else:
            return redirect('failed')

        # Создаем запись о домашнем животном клиента
        type_animal = TypeAnimal.objects.get(animal=pet_type_id)
        ClientAnimal.objects.create(age=age, description=pet_details, client=client, typeanimal=type_animal)

        # Возвращаем успешный ответ
        return redirect('success')

    times = Booking.objects.all()
    type_animals = TypeAnimal.objects.all()
    today_date = date.today().isoformat()
    return render(request, 'reg.html', {'today_date': today_date , 'type_animals': type_animals , 'times' : times})



