# Generated by Django 5.0.7 on 2024-08-17 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('certificate', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='course')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='course.category')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='account.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='session')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='course.season')),
            ],
        ),
    ]
