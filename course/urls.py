from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('<str:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('<str:slug>/<int:pk>/', views.LoadSessionView.as_view(), name='load_session'),
    path('<str:slug>/add-comment/', views.add_comment, name='add_comment'),
    path('<str:slug>/comment-list/', views.comment_list, name='comment_list'),

]