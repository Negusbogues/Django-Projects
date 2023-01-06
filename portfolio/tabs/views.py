from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from . import models
from scraper import gold_price

# Create your views here.
class HomeView(TemplateView):
        template_name = 'tabs/home.html'
def lbs2kgs(Weight):
    k = 2.20462262185
    res = round(Weight*k,2)            
    return res
def projects_view(request):
    all = models.WeightConvert.objects.all().delete()
    all1 = models.PasswordGen.objects.all().delete()
    weightinfoKG= models.WeightConvert.objects.filter(Unit= 'KG')
    weightinfoLB= models.WeightConvert.objects.filter(Unit= 'LB') 
    Pass = models.PasswordGen.objects.all()
    context = {
            "weightKG":weightinfoKG,
            "weightLB":weightinfoLB,
            "goldprice": gold_price(),
            "Pass":Pass,
            }
    if request.POST:
        try:
            Weight = request.POST['Weight']
            Unit = request.POST['Unit']
            models.WeightConvert.objects.create(Weight=Weight, Unit=Unit)    
            return render(request, 'tabs/projects.html', context)
        except:
            Length = request.POST['Length']
            Special = request.POST['Special']
            models.PasswordGen.objects.create(Length=Length, Special=Special)
            return render(request, 'tabs/projects.html', context)
    else:
        return render(request, 'tabs/projects.html', context)
    

def contact_view(request):
    context = {
        'goldprice': gold_price(),
    }
    return render(request, 'tabs/contact.html', context)
def result_view(request):
    weightinfoKG= models.WeightConvert.objects.filter(Unit= 'KG')
    weightinfoLB= models.WeightConvert.objects.filter(Unit= 'LB')
    context = {
        "weightKG":weightinfoKG,
        "weightLB":weightinfoLB,
    }
    return render(request, 'tabs/result.html', context)    