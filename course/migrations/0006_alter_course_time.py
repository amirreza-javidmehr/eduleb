# Generated by Django 5.0.7 on 2024-08-18 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_session_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
