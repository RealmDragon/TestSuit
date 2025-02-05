from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Doctor, Service, Department, Appointment, Contact
from .forms import CustomUserCreationForm, DoctorForm

import os
import django

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    django.setup()

class ModelTests(TestCase):
    """Тесты моделей."""

    def setUp(self):
        """Создаем тестовые данные перед каждым тестом."""
        self.department = Department.objects.create(name='Терапия', description='Описание терапевтического отделения', contact_info='Телефон: 123-456')
        self.doctor = Doctor.objects.create(user=User.objects.create_user('testuser', 'test@example.com', 'testpass'), specialty='Терапевт', experience=5)
        self.service = Service.objects.create(name='Консультация', description='Описание услуги', price=1000.00, category='Консультация')
        self.appointment = Appointment.objects.create(patient=User.objects.create_user('patient', 'patient@example.com', 'patientpass'), doctor=self.doctor, service=self.service, department=self.department, date_time='2024-12-31 10:00:00', status='confirmed')
        self.contact = Contact.objects.create(name='Иван Иванов', email='ivan@example.com', message='Пример сообщения')

    def test_department_creation(self):
        """Проверяем создание отдела."""
        self.assertEqual(self.department.name, 'Терапия')
        self.assertEqual(self.department.description, 'Описание терапевтического отделения')

    def test_doctor_creation(self):
        """Проверяем создание врача."""
        self.assertEqual(self.doctor.specialty, 'Терапевт')
        self.assertEqual(self.doctor.experience, 5)

    def test_service_creation(self):
        """Проверяем создание услуги."""
        self.assertEqual(self.service.name, 'Консультация')
        self.assertEqual(self.service.price, 1000.00)

    def test_appointment_creation(self):
        """Проверяем создание записи на прием."""
        self.assertEqual(self.appointment.doctor, self.doctor)
        self.assertEqual(self.appointment.service, self.service)

    def test_contact_creation(self):
        """Проверяем создание сообщения обратной связи."""
        self.assertEqual(self.contact.name, 'Иван Иванов')
        self.assertEqual(self.contact.email, 'ivan@example.com')


class ViewTests(TestCase):
    """Тесты представлений."""

    def setUp(self):
        """Создаем тестового клиента и пользователя."""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(self.user)

    def test_home_page(self):
        """Проверяем главную страницу."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_services_page(self):
        """Проверяем страницу услуг."""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main1/services.html')

    def test_about_page(self):
        """Проверяем страницу 'О нас'."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contacts_page(self):
        """Проверяем страницу контактов."""
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')

    def test_registration_page(self):
        """Проверяем страницу регистрации."""
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_departments_page(self):
        """Проверяем страницу отделений."""
        response = self.client.get(reverse('departments'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'departments.html')

    def test_doctors_page(self):
        """Проверяем страницу врачей."""
        response = self.client.get(reverse('doctors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctors.html')

    def test_add_doctor_page(self):
        """Проверяем страницу добавления врача."""
        response = self.client.get(reverse('add_doctor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_doctor.html')

    def test_edit_doctor_page(self):
        """Проверяем страницу редактирования врача."""
        doctor = Doctor.objects.create(user=User.objects.create_user('edituser', 'edit@example.com', 'editpass'), specialty='Хирург', experience=7)
        response = self.client.get(reverse('edit_doctor', args=[doctor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_doctor.html')

    def test_delete_doctor_page(self):
        """Проверяем страницу удаления врача."""
        doctor = Doctor.objects.create(user=User.objects.create_user('deluser', 'del@example.com', 'delpass'), specialty='Терапевт', experience=3)
        response = self.client.get(reverse('delete_doctor', args=[doctor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_doctor.html')


class FormTests(TestCase):
    """Тесты форм."""

    def test_custom_user_creation_form_valid(self):
        """Проверяем, что форма создания пользователя работает правильно."""
        form_data = {'username': 'newuser', 'email': 'new@example.com', 'password': 'newpassword', 'password2': 'newpassword'}
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid(self):
        """Проверяем, что форма создания пользователя не проходит валидацию при неверных данных."""
        form_data = {'username': 'newuser', 'email': 'new@example.com', 'password': 'newpassword', 'password2': 'wrongpassword'}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_doctor_form_valid(self):
        """Проверяем, что форма врача работает правильно."""
        form_data = {'user': User.objects.create_user('doctoruser', 'doctor@example.com', 'doctorpassword').pk, 'specialty': 'Кардиолог', 'experience': 10}
        form = DoctorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_doctor_form_invalid(self):
        """Проверяем, что форма врача не проходит валидацию при неверных данных."""
        form_data = {'user': None, 'specialty': '', 'experience': -1}
        form = DoctorForm(data=form_data)
        self.assertFalse(form.is_valid())

