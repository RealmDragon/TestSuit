from django.db import models

from doctor.models import Doctor
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', **NULLABLE)
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    email = models.EmailField(verbose_name='Почта')
    birth_date = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    owner = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ['-created_at']


class Record(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    record_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата записи')
    record_time = models.TimeField(verbose_name='Время записи')
    doctor = models.ForeignKey(Doctor, max_length=100, on_delete=models.CASCADE, verbose_name='Доктор')
    owner = models.ForeignKey(User, default=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    publication = models.BooleanField(default=True, verbose_name="Признак публикации")

    def __str__(self):
        return (f'{self.client.surname} {self.client.name} {self.client.patronymic} - '
                f'Вы записаны к {self.doctor} на {self.record_date} в {self.record_time}')

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        permissions = [
            ('can_add_record', 'Может добавлять запись'),
            ('can_change_record', 'Может изменять запись'),
            ('can_view_record', 'Может просматривать запись'),
            ('can_delete_record', 'Может удалять запись'),
        ]


class Diagnostics(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    diagnosis = models.CharField(max_length=300, verbose_name='Диагноз')
    test = models.CharField(max_length=200, verbose_name='Тест')
    result = models.CharField(max_length=150, verbose_name='Результат')
    units_of_measurement = models.CharField(max_length=100, verbose_name='Единицы измерения')
    proper_values = models.CharField(max_length=100, verbose_name='Должные значения')

    def __str__(self):
        return f'{self.client.surname} {self.client.name} {self.client.patronymic} - ' \
               f'Тест: {self.test}, Результат: {self.result}, Единицы измерения: {self.units_of_measurement}' \
               f'Должные значения: {self.proper_values}, Диагноз: {self.diagnosis}'

    class Meta:
        verbose_name = 'диагностика'
        verbose_name_plural = 'диагностики'
        permissions = [
            ('can_view_diagnostics', 'Может просматривать диагностики'),
        ]
