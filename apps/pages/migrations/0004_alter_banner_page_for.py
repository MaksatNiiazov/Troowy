# Generated by Django 5.0.6 on 2024-07-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_banner_alter_welcomecarsimage_content_object_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='page_for',
            field=models.CharField(choices=[('all', 'Везде'), ('properties', 'Нудвижимость'), ('cars', 'Автомобили'), ('tours', 'Туры'), ('medical_tours', 'Медицинские туры')], default='provider', max_length=200, verbose_name='Страница'),
        ),
    ]
