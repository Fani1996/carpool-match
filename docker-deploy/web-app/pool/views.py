from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .models import Ride, searchFromSharer
from .forms import RideModelForm, SearchSharerModelForm


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


# View for editing ride details
def editView(request, pk):
    post = get_object_or_404(Ride, pk=pk)
    if request.method == "POST":
       form = RideModelForm(request.POST, instance=post)
       if form.is_bound and form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('pool:rider')
    else:
        form = RideModelForm(instance=post)


        
    return render(request, 'pool/edit.html', {'form': form})


# View for detail of a ride
def detailView(request, pk):
    post = get_object_or_404(Ride, pk=pk)
    form = RideModelForm(instance=post)
    #last_url = request.META.get('HTTP_REFERER')
    return render(request, 'pool/detail.html', {'form': form,'ride': post,}) #'url':last_url})


def searchResultView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    results = Ride.objects.filter(arrival_time__lte=timezone.now()).order_by('-arrival_time')

    #results = Ride.objects.filter(destination=)
    return render(request, 'pool/search_results.html', {'results': results})


class DetailView(generic.DetailView):
    model = Ride
    template_name = 'pool/detail.html'

    def get_queryset(self):
        return Ride.objects.filter(arrival_time__lte=timezone.now())


# Rider page view
def riderView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    rides = Ride.objects.filter(sharer=request.user).order_by('-arrival_time')
    
    if request.method == "POST":
        form = RideModelForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.owner = request.user
            post.save()
            post.sharer.add(request.user)
            post.save()
            return redirect('pool:rider')
    else:
        form = RideModelForm()

    return render(request, 'pool/index.html', {'latest_question_list': rides, 'user': request.user, 'form': form})


# Driver Page view
def driverView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.driver or request.user.license_plate_number == '' or request.user.capacity == '' or request.user.vehicle_type == '':
        return redirect('profile')
    
    rides_his = Ride.objects.filter(driver=request.user).order_by('-arrival_time')
    avail_rides = rides_his    
    
    if request.user.optional_info == '':
        avail_rides = Ride.objects.filter(driver__isnull=True, passenger_count__lte=request.user.capacity,
                                          special_request__isnull=True,
                                          is_confirmed=False,
                                          vehicle_type__in=['', request.user.vehicle_type]).exclude(owner=request.user).exclude(sharer__username__contains=request.user.username)

    else:
        avail_rides = Ride.objects.filter(driver__isnull=True, passenger_count__lte=request.user.capacity,
                                          special_request=request.user.optional_info,
                                          is_confirmed=False,
                                          vehicle_type__in=['', request.user.vehicle_type]).exclude(owner=request.user).exclude(sharer__username__contains=request.user.username)
        
    if request.method == "POST":
        form = RideModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('pool:driver')
    else:
        form = RideModelForm()

    return render(request, 'pool/driver.html', {'latest_question_list': rides_his, 'avail_rides': avail_rides, 'user': request.user, 'form': form})



# Search form and search results are displayed
def searchView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    rides = None

    if request.method == "POST":
        searchform = SearchSharerModelForm(request.POST)

        if searchform.is_valid():
            post = searchform.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()

            ride_res = Ride.objects.filter(destination=post.destination,
                                           passenger_count=post.passenger_count,
                                           is_completed=False, is_confirmed=False,
                                           can_shared=True, 
                                           arrival_time__gte=post.earliest_arrival_time,
                                           arrival_time__lte=post.latest_arrival_time).exclude(owner=request.user).exclude(driver=request.user).exclude(sharer__username__contains=request.user.username)
            
        
            return render(request, 'search_results.html', {'results':ride_res})
    else:
        searchform = SearchSharerModelForm()

    return render(request, 'pool/search.html', {'latest_question_list': rides, 'form': searchform})



# Confirm ride view
def ConfirmRide(request, pk):
    
    post = get_object_or_404(Ride, pk=pk)

    # make sure it is proper user to claim the ride
    if request.user in post.sharer.all() or request.user==post.owner or request.user.driver==False or request.user.license_plate_number=='' or request.user.vehicle_type=='' or request.user.capacity < post.passenger_count:
        return redirect('home')
        

    post.driver = request.user
    post.is_confirmed = True
    post.vehicle_type = request.user.vehicle_type
    post.license_plate_number = request.user.license_plate_number
    post.capacity = request.user.capacity
    post.driver_real_name = request.user.real_name

    sharer_list = post.sharer;
    mail_list = []
    for user in sharer_list.all():
        mail_list.append(user.email)
    send_mail('Carpool Ride Confirmed',
              'Your carpool ride is confirmed, please go online and check!',
              settings.EMAIL_HOST_USER,
              mail_list,
              fail_silently=True,)
        
    post.save()

    return redirect('pool:driver')


# Complete ride
def CompleteRide(request, pk):

    post = get_object_or_404(Ride, pk=pk)

    if not request.user == post.driver:
        return redirect('home')
    
    post.is_completed = True
    post.save()

    return redirect('pool:driver')


# Join Ride
def JoinRide(request, pk):
    post = get_object_or_404(Ride, pk=pk)
    post.sharer.add(request.user)
    post.passenger_count += 1;
    post.save()
    return redirect('pool:rider')
