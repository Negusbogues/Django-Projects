from django.contrib import admin
from .models import WeightConvert, PasswordGen, Contact, BMI
# Register your models here.
admin.site.register(WeightConvert)
admin.site.register(Contact)
admin.site.register(PasswordGen)
admin.site.register(BMI)