from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('submit/', views.SubmitPageView.as_view(), name='submit'),
    path('logout/', views.LogoutUserView.as_view(), name='logout')
]