import random
from string import ascii_letters
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