from django.db import models

from account.models import Teacher


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='%(class)s')
    time = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    certificate = models.BooleanField(default=False)
    image = models.ImageField(upload_to='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s')

    def __str__(self):
        return self.title

class Session(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='session')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='%(class)s')

    def __str__(self):
        return self.title


