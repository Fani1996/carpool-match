from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    #change_form = CustomUserChangeForm
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        ('Real Name', {
            'fields': ('real_name',)
        }),
        ('Driver Status', {
            'fields': ('driver',)
        }),        
        ('Vehicle Info', {
            'fields': ('vehicle_type','license_plate_number', 'capacity', 'optional_info',)
        }),
    ) 
    
#    fieldsets = UserAdmin.fieldsets #(None, {'fields':('real_name')})
    list_display = ['username', 'real_name', 'driver', 'vehicle_type', 'license_plate_number', 'optional_info' ]

admin.site.register(CustomUser, CustomUserAdmin)
