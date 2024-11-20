# Generated by Django 5.0.7 on 2024-08-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Dirección Web'),
        ),
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='subtítulo'),
        ),
    ]
