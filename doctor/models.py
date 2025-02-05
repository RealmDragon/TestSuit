from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Doctor(models.Model):
    avatar = models.ImageField(upload_to='doctor/', **NULLABLE)
    name = models.CharField(max_length=255, verbose_name='Имя доктора')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество доктора', **NULLABLE)
    surname = models.CharField(max_length=255, verbose_name='Фамилия доктора')
    age = models.PositiveIntegerField(verbose_name='Возраст', **NULLABLE)
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    qualification = models.CharField(max_length=255, verbose_name='Квалификация')
    experience = models.PositiveIntegerField(verbose_name='Опыт работы в летах')

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}, {self.specialization}, {self.qualification}'

    class Meta:
        verbose_name = 'доктор'
        verbose_name_plural = 'доктора'
