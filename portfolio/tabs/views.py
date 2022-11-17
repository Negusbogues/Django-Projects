from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from . import models


# Create your views here.
class HomeView(TemplateView):
        template_name = 'tabs/home.html'

def about_view(request):
    return render(request, 'tabs/about.html')