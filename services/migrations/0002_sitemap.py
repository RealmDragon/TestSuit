# Generated by Django 5.0.7 on 2024-08-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitemap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Описание')),
                ('travel_map', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Карта сайта',
                'verbose_name_plural': 'Карты сайта',
            },
        ),
    ]
