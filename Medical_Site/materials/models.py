from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('main.Service', on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')])

    def __str__(self):
        return f"{self.user.username} - {self.service.name} - {self.date}"

