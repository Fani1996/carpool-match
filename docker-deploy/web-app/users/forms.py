from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',
                                                 'real_name',
                                                 'driver',
                                                 'vehicle_type',
                                                 'license_plate_number',
                                                 'capacity',
                                                 'optional_info',)

        widgets = {
            'vehicle_type': forms.Select(attrs={
                'class': 'form-control',
            },choices=[('Sedan', 'Sedan'),('SUV', 'SUV'),('Van', 'Van'),('Bus', 'Bus'),]),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields =  ('email', 'real_name', 'driver',
                   'vehicle_type', 'license_plate_number',
                   'capacity',
                   'optional_info',)

        widgets = {
            'vehicle_type': forms.Select(attrs={
                'class': 'form-control',
            },choices=[('Sedan', 'Sedan'),('SUV', 'SUV'),('Van', 'Van'),('Bus', 'Bus'),]),
        }
