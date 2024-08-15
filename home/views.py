from django.shortcuts import render
from django.views.generic import View ,TemplateView


class HomePageView(TemplateView):
    template_name = 'home/index.html'