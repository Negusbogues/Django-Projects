from django import forms
from .models import Consult, Review, AType, Order

class ConsultForm(forms.ModelForm):
    class Meta:
        model = Consult
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

class ServiceOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
    