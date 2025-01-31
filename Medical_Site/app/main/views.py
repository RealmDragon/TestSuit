from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Doctor, Department, MedicalService

def home(request):
    return render(request, 'index.html')

def services(request):
    services = MedicalService.objects.all()
    return render(request, 'main/services.html', {'services': services})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors})

def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})

def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'edit_doctor.html', {'form': form})

def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    return render(request, 'delete_doctor.html', {'doctor': doctor})