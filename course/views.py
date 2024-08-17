from django.shortcuts import render
from django.views.generic import ListView
from course.models import Course, Season, Session


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 5
