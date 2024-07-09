# Generated by Django 5.0.6 on 2024-05-13 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysector',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='document',
            name='company_sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.companysector', verbose_name='Сектор компании'),
        ),
        migrations.AddField(
            model_name='companysector',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.sector', verbose_name='Сектор'),
        ),
    ]
