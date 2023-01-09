from django import forms
from .models import WeightConvert, BMI, PasswordGen

class WeightForm(forms.ModelForm):
    edit_weight = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = WeightConvert
        fields = "__all__"

class BMI(forms.Form):
    class Meta:
        model = BMI
        fields = "__all__"

class PasswordGen(forms.ModelForm):
    edit_pass = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = PasswordGen
        fields = "__all__"