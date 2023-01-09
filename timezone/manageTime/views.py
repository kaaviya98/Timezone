from django.shortcuts import render,redirect
from django.utils import timezone,dateformat
from .forms import CityForm
from datetime import datetime as dt
import pytz
from pytz import timezone


    

   


def displayview(request):
    form = CityForm()
    if request.method=='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            city_name = cd.get('Select_a_city')
    else:
        city_name ="dummy"
    zone=pytz.timezone("UTC")
    standard_time=dt.now(zone)
    d=standard_time.astimezone(timezone(city_name))
    print(d)
    
    current_time=d.strftime("%b %d, %Y %-I:%M:%S%p ")
    return render(
        request,
        "manageTime/display.html",
        {"city":city_name,"time": current_time},
    )

def changecityview(request):
    cities={"Chennai","Mumbai"}
    return render(
        request,
        "manageTime/change_city.html",
        {"city": cities,
        "city_form": CityForm},
    )

# def form_handle(request):
#     form = MyForm()
#     if request.method=='POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             #now in the object cd, you have the form as a dictionary.
#             a = cd.get('a')from django.shortcuts import redirect, render

# Prepare a map of common locations to timezone choices you wish to offer.
common_timezones = {
    'London': 'Europe/London',
    'Paris': 'Europe/Paris',
    'New York': 'America/New_York',
}

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': common_timezones})