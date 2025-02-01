import os
import django

# Установите переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.config.settings")

# Инициализируйте Django
django.setup()

# Теперь вы можете импортировать и использовать Django модели и другие компоненты
from django.core.management import call_command
from django.test import TestCase
from app.main.models import Department, Service, Contact, Doctor, MedicalService

class ModelTests(TestCase):

    def test_create_department(self):
        department = Department.objects.create(name="Test Department", description="Test Description")
        self.assertEqual(department.name, "Test Department")
        self.assertEqual(department.description, "Test Description")

    def test_create_service(self):
        service = Service.objects.create(name="Test Service", description="Test Description", price=100)
        self.assertEqual(service.name, "Test Service")
        self.assertEqual(service.description, "Test Description")
        self.assertEqual(service.price, 100)

    def test_create_contact(self):
        contact = Contact.objects.create(address="Test Address", phone="123-456-7890", email="test@test.com")
        self.assertEqual(contact.address, "Test Address")
        self.assertEqual(contact.phone, "123-456-7890")
        self.assertEqual(contact.email, "test@test.com")

    def test_create_doctor(self):
        department = Department.objects.create(name="Test Department", description="Test Description")
        doctor = Doctor.objects.create(name="Test Doctor", specialty="Test Specialty", experience=5, department=department)
        self.assertEqual(doctor.name, "Test Doctor")
        self.assertEqual(doctor.specialty, "Test Specialty")
        self.assertEqual(doctor.experience, 5)

    def test_create_medicalservice(self):
        service = MedicalService.objects.create(name="Test Medical Service", description="Test Description", price=100)
        self.assertEqual(service.name, "Test Medical Service")
        self.assertEqual(service.description, "Test Description")
        self.assertEqual(service.price, 100)