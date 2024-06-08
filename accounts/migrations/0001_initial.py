# Generated by Django 4.2.13 on 2024-06-06 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('current_time', models.TimeField(default=django.utils.timezone.now)),
                ('current_date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
