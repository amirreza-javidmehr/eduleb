from .mixins import IsAuthenticatedMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import SubmitUserForm, LoginUserForm
from .models import User
from django.contrib.auth import login , logout , authenticate

class LoginPageView(IsAuthenticatedMixin, View):
    def get(self, request):
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form':form})

    def post(self, request):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = authenticate(phone=phone, password=password)
            login(request, user)
            return redirect('home:main')
        return render(request, 'account/login.html', {'form':form})



class SubmitPageView(IsAuthenticatedMixin, View):
    def get(self, request):
        form = SubmitUserForm()
        return render(request, 'account/submit.html', {'form':form})

    def post(self, request):
        form = SubmitUserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = User.objects.create_user(phone=form_data['phone'], password=form_data['password'])
            login(request, user)
            return redirect('home:main')
        return render(request, 'account/submit.html', {'form': form})

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('home:main')

