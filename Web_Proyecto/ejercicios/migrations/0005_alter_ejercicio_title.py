# Generated by Django 5.0.7 on 2024-08-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicios', '0004_alter_ejercicio_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Título'),
        ),
    ]