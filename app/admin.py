from django.contrib import admin
from app.models import Doctor, Service, Department, Appointment


#Inline модели
class AppointmentInline(admin.StackedInline):
    model = Appointment
    extra = 1

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'experience')
    inlines = [AppointmentInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'service', 'date_time', 'status')
    list_filter = ('status', 'doctor', 'service', 'date_time')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    readonly_fields = ('created_at',)