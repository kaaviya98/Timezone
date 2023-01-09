from django import forms
import pytz

CITY_CHOICES= [
    ('Africa/Abidjan', 'Africa/Abidjan'),
    ('US/Newyork', 'US/Newyork'),
    ('Asia/Kolkata', 'Asia/Kolkata'),
    ('Europe/Berlin', 'Europe/Berlin'),
     ('Singapore', 'Singapore'),

    ]

class CityForm(forms.Form):
    Select_a_city= forms.CharField( widget=forms.Select(choices=CITY_CHOICES))