from django.db import models
from django.core import validators

class Consult(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Delivery_Date = models.DateField(help_text = 'YYYY-MM-DD format')
    Notes = models.CharField(max_length=200, null= True)

    
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} has an order. Delivery Date: {self.Delivery_Date}."

class AType(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'
    FOUR = 4, '4'
    FIVE = 5, '5'
    SIX = 6, '6'
    SEVEN = 7, '7'
    EIGHT = 8, '8'
    NINE = 9, '9'
    TEN = 10, '10'
    ELEVEN = 11,'11'
    TWELVE = 12, '12'
    THIRTEEN = 13, '13'
    FOURTEEN = 14, '14'
    FIFTEEN =15, '15'
    SIXTEEN=16, '16'
    SEVENTEEN=17, '17'
    EIGHTTEEN=18, '18'
    NINETEEN=19, '19'
    TWENTY=20, '20'
    TWENTYONE=21, '21'
    TWENTYTWO=22, '22'
    TWENTYTHREE=23, '23'
    TWENTYFOUR=24, '24'
    TWENTYFIVE=25, '25'
    TWENTYSIX=26, '26'
    TWENTYSEVEN=27, '27'
    TWENTYEIGHT=28, '28'
    TWENTYNINE=29, '29'
    THRITY=30, '30'
    THRITYONE=31, '31'
    THRITYTEO=32, '32'
    THRITYTHREE=33, '33'
    THRITYFOUR=34, '34'
    THRITYFIVE=35, '35'


class BType(models.IntegerChoices):
    ONE = 1, '1'
    TWO = 2, '2'
    THREE = 3, '3'

class Review(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Rating = models.IntegerField(choices=AType.choices)

class Checkout(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Address =models.CharField(max_length=200)
    City =models.CharField(max_length=100)
    State =models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Delivery_Date = models.DateField(help_text = 'YYYY-MM-DD format')


class Order(models.Model):
    Id_Number = models.AutoField(primary_key=True)
    Quantity = models.IntegerField(choices=AType.choices)
    Notes = models.CharField(max_length=150, null= True)
    Item = models.CharField(max_length=100)
    Price = models.DecimalField(decimal_places=2, max_digits=6)
    Total = models.DecimalField(decimal_places=2, max_digits=6)
    @property
    def total_cost(self):
        return self.Quantity * self.Price
    
    def sub_total(self, order):
        total = self.total_cost
        total += order.total_cost
        return round(total,2)

