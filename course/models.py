from django.db import models
from django.template.defaulttags import comment
from django.urls import reverse
from django.utils.text import slugify
from account.models import Teacher, User

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
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(str(self.title), allow_unicode=True)
        if self.session.name != None:
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

    def get_absolute_url(self):
        return reverse('course:course_detail', args=[self.slug])

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

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='%(class)s')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]


