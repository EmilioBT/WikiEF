# Generated by Django 5.0.7 on 2024-08-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicios', '0005_alter_ejercicio_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
