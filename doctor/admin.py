from django.contrib import admin

from doctor.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'patronymic', 'surname', 'specialization', 'qualification', 'experience']
