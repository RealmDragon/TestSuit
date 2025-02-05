from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью User
    specialty = models.CharField(max_length=255)
    experience = models.IntegerField()
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255) # Например, "Диагностика", "Лечение" и т.д.
    photo = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    contact_info = models.TextField()  # Можно хранить телефон, email

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Ожидает подтверждения'), ('confirmed', 'Подтверждено'), ('cancelled', 'Отменено')])


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)