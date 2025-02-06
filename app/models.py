
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Use get_user_model() for User

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.address

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='doctors/')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed')
        ]
    )

    def __str__(self):
        return f"{self.user.username} - {self.service.name} - {self.date}"