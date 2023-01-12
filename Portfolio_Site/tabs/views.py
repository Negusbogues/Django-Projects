from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, FormView, CreateView
from django.urls import reverse_lazy, reverse
from . import models
from scraper import gold_price
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
class HomeView(TemplateView):
        template_name = 'tabs/home.html'
def lbs2kgs(Weight):
    k = 2.20462262185
    res = round(Weight*k,2)            
    return res
def projects_view(request):
    bmi_clean = models.BMI.objects.all().delete()
    weight_clean = models.WeightConvert.objects.all().delete()
    pass_clean = models.PasswordGen.objects.all().delete()
    weightinfoKG= models.WeightConvert.objects.filter(Unit= 'KG')
    weightinfoLB= models.WeightConvert.objects.filter(Unit= 'LB') 
    Pass = models.PasswordGen.objects.all()
    BMI = models.BMI.objects.all()
    context = {
            "weightKG":weightinfoKG,
            "weightLB":weightinfoLB,
            "goldprice": gold_price(),
            "Pass":Pass,
            "BMI":BMI,
            }
    if request.method == 'POST':
        if 'BMI' in request.POST:
            Weight = request.POST['Weight']
            Unit = request.POST['Unit']
            Feet = request.POST['Feet']
            Inches = request.POST['Inches']
            Sex = request.POST['Sex']
            models.BMI.objects.create(Weight=Weight, Unit=Unit, Feet=Feet, Inches=Inches, Sex=Sex)    
            return render(request, 'tabs/projects.html', context)
        if 'WeightCon' in request.POST:
            Weight = request.POST['Weight']
            Unit = request.POST['Unit']
            models.WeightConvert.objects.create(Weight=Weight, Unit=Unit)    
            return render(request, 'tabs/projects.html', context)
        if 'Password' in request.POST:
            Length = request.POST['Length']
            Special = request.POST['Special']
            models.PasswordGen.objects.create(Length=Length, Special=Special)
            return render(request, 'tabs/projects.html', context)
    else:
        return render(request, 'tabs/projects.html', context)
def contact_view(request):
    try:
        if request.POST:
            Subject = request.POST['Subject']
            Message = request.POST['Message']
            From = settings.EMAIL_HOST_USER
            To = request.POST['To']
            recipient_list=[To]
            models.Contact.objects.create(Subject=Subject, Message=Message, From=From, To=To)
            '''send_mail(
                subject=Subject,
                message=Message,
                from_email=From,
                recipient_list=[To]
            )'''
            return redirect(reverse('tabs:thank_you'))
        else:
            return render(request, 'tabs/contact.html')
    except(ValueError):
        return render(request, 'tabs/contact.html')
def resume_view(request):
    return render(request, 'tabs/resume.html')  
def certifications_view(request):
    return render(request, 'tabs/certifications.html')
def thank_you_view(request):
    return render(request, 'tabs/thank_you.html')  