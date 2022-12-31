from django import forms
from .models import WeightConvert, UnitType

class WeightForm(forms.ModelForm):
    class Meta:
        model = WeightConvert
        fields = "__all__"