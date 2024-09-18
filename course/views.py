from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from course.models import Course, Season, Session, Category, Comment


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 5

class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

class LoadSessionView(View):
    def get(self, request, pk, slug):
        session = Session.objects.get(id=pk).video.url
        return JsonResponse({"session": session})

def add_comment(request, slug):
   if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.first_name == None:
            request.user.first_name = request.POST.get("first_name")
            request.user.save()
        if request.user.last_name == None:
            request.user.last_name = request.POST.get("last_name")
            request.user.save()
        if request.user.email == None:
            request.user.email = request.POST.get("email")
            request.user.save()
        rate = request.POST.get("rate")
        if rate != "":
            rate = int(rate)
        else:
            rate = 5
        parent_id = request.POST.get("parent_id")
        if parent_id != "":
            parent = Comment.objects.get(id=int(parent_id))
        else:
            parent = None
        body = request.POST.get("body")
        course = Course.objects.get(slug=slug)
        Comment.objects.create(user=request.user, course= course ,rate=rate, parent=parent ,body=body)
        return JsonResponse({"message": "success"})

def comment_list(request, slug):
    course = Course.objects.get(slug=slug)
    comments = Comment.objects.filter(course=course)
    paginator = Paginator(comments, 10)
    page_number = request.GET.get('page')
    object_list = paginator.get_page(page_number)
    if comments:
        rate_list = comments.values_list('rate')
        sum = 0
        for rate in rate_list:
           sum += int(rate[0])
        avg = sum / len(rate_list)
        course.rate = avg
        course.save()
    return render(request, "course/comment_list.html", {"comments": object_list, 'course': course})
