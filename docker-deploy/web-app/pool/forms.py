from django import forms
from django.forms import ModelForm
from .models import Ride, searchFromSharer, CustomUser
from .selectTimeWidget import SelectTimeWidget


class RideModelForm(ModelForm):
    class Meta(object):
        model = Ride
        fields = ['start_location', 'destination', 'arrival_time',
                  'passenger_count', 'vehicle_type', 'can_shared', 'special_request',
        ]

        widgets = {
            'start_location': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'arrival_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Format: "Year-Month-Date Hour:Minute"'
            }),
            'passenger_count': forms.NumberInput(attrs={
                'class': 'form-contrl'
            }),
            'vehicle_type': forms.Select(attrs={
                'class': 'form-control',
            },choices=[('',''),   ('Sedan', 'Sedan'),('SUV', 'SUV'),('Van', 'Van'),('Bus', 'Bus'),]),
            'can_shared': forms.CheckboxInput(attrs={
               'class': 'form-control'
            }),
            'special_request': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

#    def __init__(self, *args, **kwargs):
#        owner = kwargs.pop('user')
#        super(RideModelForm, self).__init__(*args, **kwargs)


class SearchSharerModelForm(ModelForm):
    class Meta(object):
        model = searchFromSharer
        fields = '__all__'

        widgets = {
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Destination'
            }),
            'earliest_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Desired Earliest Arrival Time'
            }),
            'latest_time': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Desired Latest Arrival Time'
            }),
            'passenger_count': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Passenger Count'
            }),
        }
