# Generated by Django 5.0.6 on 2024-07-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_propertytype_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertytype',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='images/categories/icons/', verbose_name='Иконка'),
        ),
    ]
