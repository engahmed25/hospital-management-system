from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm ,LoginForm
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
        print('Registration x')
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('valid username or password')
                return redirect('home')  # Replace 'home' with your home page URL name
    else:
        print('Invalid username or password')
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

from django.shortcuts import render
from clinic.models import Clinic
from doctor.models import Doctor
def home(request):
    clinics = Clinic.objects.all()[:3]  # Limit to 3 clinics
    doctors = Doctor.objects.all()[:3]  # Limit to 3 doctors
    return render(request, 'home.html', {'clinics': clinics, 'doctors': doctors})

def user_logout(request):
    logout(request)
    return redirect('login') 



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})



from django.shortcuts import render
from clinic.models import Clinic
from doctor.models import Doctor
from .forms import UnifiedSearchForm
def unified_search(request):
    form = UnifiedSearchForm(request.GET or None)
    clinics = []
    doctors = []

    if form.is_valid():
        query = form.cleaned_data['query']
        clinics = Clinic.objects.filter(name__icontains=query)
        doctors = Doctor.objects.filter(full_name__icontains=query)

    return render(request, 'account/unified_search.html', {'form': form, 'clinics': clinics, 'doctors': doctors})