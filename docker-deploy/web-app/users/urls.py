# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('/', views.profile, name=''),
    path('profile/', views.profile, name='profile'),
]
