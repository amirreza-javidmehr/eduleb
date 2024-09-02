from django.db import models
from django.utils.text import slugify
from account.models import Teacher
import datetime

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='%(class)s')
    time = models.TimeField(blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    certificate = models.BooleanField(default=False)
    image = models.ImageField(upload_to='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(str(self.title), allow_unicode=True)
        sessions = self.session.all()
        time = 0
        for session in sessions:
            tm = str(session.time)
            timeParts = [int(s) for s in tm.split(':')]
            time += ((timeParts[0] * 60) + (timeParts[1] * 60)) + timeParts[2]
        time, sec = divmod(time, 60)
        hr, min = divmod(time, 60)
        self.time = "%d:%02d:%02d" % (hr, min, sec)
        super(Course, self).save()

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
    course = models.ForeignKey(Course, default='',on_delete=models.CASCADE, related_name='%(class)s')
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title


