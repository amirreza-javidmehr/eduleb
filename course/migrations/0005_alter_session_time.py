# Generated by Django 5.0.7 on 2024-08-18 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_session_course_session_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
