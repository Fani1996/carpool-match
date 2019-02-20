from django.urls import path

from . import views

app_name = 'pool'

urlpatterns = [
    # path('', views.riderView, name='index'),
    path('<int:pk>/detail/edit/', views.editView, name='ride_edit'),
    path('<int:pk>/detail/', views.detailView, name='detail'),
    path('result/', views.searchResultView, name='search_result'),
    path('search/', views.searchView, name='search'),
    path('rider/', views.riderView, name='rider'),
    path('driver/', views.driverView, name='driver'),
    path('<int:pk>/confirm/', views.ConfirmRide, name='confirm'),
    path('<int:pk>/complete/', views.CompleteRide, name='complete'),
    path('<int:pk>/join/', views.JoinRide, name='join'),
]
