from django.shortcuts import render, redirect, render_to_response
# users/views.py
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



#class ChangeProfile(generic.CreateView):
#    form_class = CustomUserChangeForm
#    success_url = reverse_lazy('pool:index')
#    template_name = 'profile.html'
    
#def profile(request):
#    response = ChangeProfile.as_view()(request)  
#    if not request.user.is_authenticated:
#        return redirect('home')
#    return response

def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home'))

    else:
        form = CustomUserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profile.html', args)
