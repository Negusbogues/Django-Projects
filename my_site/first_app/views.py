from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView, FormView, CreateView
from .forms import ConsultForm, ReviewForm
from django.urls import reverse_lazy, reverse
from . import models


# Create your views here.
class HomeView(TemplateView):
        template_name = 'first_app/home.html'

def contact_view(request):
    if request.POST:
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email = request.POST['Email']
        Phone = int(request.POST['Phone'])
        Delivery_Date = request.POST['Delivery_Date']
        Notes = request.POST['Notes']
        models.Consult.objects.create(First_Name=First_Name, Last_Name=Last_Name, Email=Email, Phone=Phone, Delivery_Date=Delivery_Date, Notes=Notes)
        return redirect(reverse('first_app:thank_you'))
    else:
        return render(request, 'first_app/contact.html')

def reviews_view(request):
    if request.POST:
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email = request.POST['Email']
        Rating = request.POST['Rating']
        models.Review.objects.create(First_Name=First_Name, Last_Name=Last_Name, Email=Email, Rating=Rating)
        return redirect(reverse('first_app:thank_you'))
    else:
        return render(request, 'first_app/reviews.html')

def services_view(request):
    if request.POST:
        Quantity = request.POST['Quantity']
        Notes = request.POST['Notes']
        Item = request.POST['Item']
        Price = request.POST['Price']
        Total = float(Quantity)*float(Price)
        models.Order.objects.create(Quantity=Quantity, Notes=Notes, Item=Item, Price=Price, Total=Total)
        return redirect(reverse('first_app:thank_you'))
    else:
        return render(request, 'first_app/services.html')

def thank_you_view(request):
    return render(request, 'first_app/thank_you.html')

def about_view(request):
    return render(request, 'first_app/about.html')

def checkout_view(request):
    all_orders= models.Order.objects.all()
    order_sum = 0.0
    for order in all_orders:
        order_sum += round(float(order.Total),2)
    context = {
        "orders": all_orders,
        "sum":order_sum,
    }
    if request.POST:
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Address = request.POST['Address']
        City = request.POST['City']
        State = request.POST['State']
        Email = request.POST['Email']
        Phone = request.POST['Phone']
        Delivery_Date = request.POST['Delivery_Date']
        models.Checkout.objects.create(First_Name=First_Name, Last_Name=Last_Name, Email=Email, Address=Address, City=City, State=State, Phone=Phone, Delivery_Date=Delivery_Date)
        return redirect(reverse('first_app:thank_you'))
    else:
        return render(request, 'first_app/checkout.html', context)

def cart_view(request):
    all_orders= models.Order.objects.all()
    order_sum = 0.0
    for order in all_orders:
        order_sum += round(float(order.total_cost),2)
    context = {
        "orders": all_orders,
        "sum":order_sum,
    }
    if request.POST:
        try:
            Id_Number = request.POST['Id_Number']
            models.Order.objects.get(Id_Number=Id_Number).delete()
            return redirect(reverse('first_app:cart'))
        except: 
            try:
                checkout = request.POST['checkout']
                return redirect(reverse('first_app:checkout'))
            except:
                print('pk not found!')
                return redirect(request, 'first_app/cart.html')
    else:
        return render(request, 'first_app/cart.html', context)

