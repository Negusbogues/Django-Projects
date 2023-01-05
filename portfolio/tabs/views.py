from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from . import models


# Create your views here.
class HomeView(TemplateView):
        template_name = 'tabs/home.html'
def lbs2kgs(Weight):
    k = 2.20462262185
    res = round(Weight*k,2)            
    return res
def projects_view(request):
    if request.POST:
        try:
            all = models.WeightConvert.objects.all().delete()
            Weight = request.POST['Weight']
            Unit = request.POST['Unit']
            models.WeightConvert.objects.create(Weight=Weight, Unit=Unit)
            weightinfoKG= models.WeightConvert.objects.filter(Unit= 'KG')
            weightinfoLB= models.WeightConvert.objects.filter(Unit= 'LB')       
            context = {
            "weightKG":weightinfoKG,
            "weightLB":weightinfoLB,
            }
            return render(request, 'tabs/projects.html', context)
        except:
            all1 = models.PasswordGen.objects.all().delete()
            Length = request.POST['Length']
            Special = request.POST['Special']
            models.PasswordGen.objects.create(Length=Length, Special=Special)
            Pass = models.PasswordGen.objects.all()
            context = {
            "Pass":Pass,
            }
            return render(request, 'tabs/projects.html', context)
    else:
        return render(request, 'tabs/projects.html')
    

def contact_view(request):
    return render(request, 'tabs/contact.html')
def result_view(request):
    weightinfoKG= models.WeightConvert.objects.filter(Unit= 'KG')
    weightinfoLB= models.WeightConvert.objects.filter(Unit= 'LB')
    context = {
        "weightKG":weightinfoKG,
        "weightLB":weightinfoLB,
    }
    return render(request, 'tabs/result.html', context)    