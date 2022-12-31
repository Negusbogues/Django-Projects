from django.db import models

# Create your models here.

class WeightConvert(models.Model):
    CHOICES = (
        ('KG', 'KG'),
        ('LB', 'LB'),
    )
    Weight = models.IntegerField()
    Unit = models.CharField(max_length=100, choices=CHOICES)
    @property
    def Kg2Lb(self):
        k = 2.20462262185
        res = round(self.Weight*k,2)            
        return res
    def Lb2Kg(self):
        l = 0.45359237
        res = round(self.Weight*l,2)            
        return res