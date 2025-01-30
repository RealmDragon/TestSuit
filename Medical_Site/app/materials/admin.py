from django.contrib import admin
from .models import Course, Lesson, Appointment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Appointment)