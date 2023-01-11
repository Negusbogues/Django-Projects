import random
from string import ascii_letters
from django.db import models

# Create your models here.
class BMI(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CHOICES1 = (
        ('KG', 'KG'),
        ('LB', 'LB'),
    )
    Feet = models.IntegerField()
    Inches = models.IntegerField()
    Weight = models.IntegerField()
    Sex = models.CharField(max_length=100, choices=CHOICES)
    Unit = models.CharField(max_length=100, choices=CHOICES1)
    @property
    def bmicalc(self):
        
        if self.Sex == 'Male':
            if self.Unit == 'KG':
                height =(((self.Feet*12)+self.Inches)*2.54)/100
                bmi = (self.Weight)/((height)*(height))
                bmi = round(bmi,2)
                if bmi <= 18.5:
                    return str(bmi)+' - Underweight'
                elif 25 > bmi > 18.5:
                    return str(bmi)+' - Normal Weight'
                elif bmi > 30:
                    return str(bmi)+ ' - Obese'
                else:
                    return str(bmi)+' - Overweight'
            else:
                height =(((self.Feet*12)+self.Inches)*2.54)/100
                l = 0.45359237
                weight = round(self.Weight*l,2)
                bmi = (weight)/((height)*(height))
                bmi = round(bmi,2)
                if bmi <= 18.5:
                    return str(bmi)+' - Underweight'
                elif 25 > bmi > 18.5:
                    return str(bmi)+' - Normal Weight'
                elif bmi > 30:
                    return str(bmi)+ ' - Obese'
                else:
                    return str(bmi)+' - Overweight'
        else:
            if self.Unit == 'KG':
                height =(((self.Feet*12)+self.Inches)*2.54)/100
                bmi = (self.Weight)/((height)*(height))
                bmi = round(bmi,2)
                if bmi <= 18.5:
                    return str(bmi)+' - Underweight'
                elif 25 > bmi > 18.5:
                    return str(bmi)+' - Normal Weight'
                elif bmi > 30:
                    return str(bmi)+ ' - Obese'
                else:
                    return str(bmi)+' - Overweight'
            else:
                height =(((self.Feet*12)+self.Inches)*2.54)/100
                l = 0.45359237
                weight = round(self.Weight*l,2)
                bmi = (weight)/((height)*(height))
                bmi = round(bmi,2)
                if bmi <= 18.5:
                    return str(bmi)+' - Underweight'
                elif 25 > bmi > 18.5:
                    return str(bmi)+' - Normal Weight'
                elif bmi > 30:
                    return str(bmi)+ ' - Obese'
                else:
                    return str(bmi)+' - Overweight'
class Contact(models.Model):
    Subject = models.CharField(max_length=250)
    Message = models.CharField(max_length=250)
    From = models.EmailField()
    To = models.EmailField()
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
class PasswordGen(models.Model):
    Length = models.IntegerField()
    Special = models.BooleanField()
    def make_password(self):
        code = ''
        passcode = []
        SpecialChar = ["!","@","#","$","%","^","&","*","(",")","-","?"]
        if self.Special == True:
            for i in range(int(self.Length)):
                if len(passcode) < (self.Length/3):
                    passcode.insert(random.randint(0, self.Length), random.choice(ascii_letters))
                elif len(passcode) < ((self.Length/3)*2):
                    passcode.insert(random.randint(0, self.Length), (random.randint(0,10)))
                else:
                    passcode.insert(random.randint(0, self.Length), random.choice(SpecialChar))
            for i in passcode:
                code = code + str(i)
        else:
            for i in range(int(self.Length)):
                if len(passcode) < (self.Length/2):
                    passcode.insert(random.randint(0, self.Length), random.choice(ascii_letters))
                else:
                    passcode.insert(random.randint(0, self.Length), (random.randint(0,10)))
            for i in passcode:
                code = code + str(i)

        return code