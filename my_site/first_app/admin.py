from django.contrib import admin
from .models import Order, Review, Consult, Checkout
# Register your models here.
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Consult)
admin.site.register(Checkout)