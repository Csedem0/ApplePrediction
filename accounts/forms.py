from django import forms
from .models import Prediction

class PredForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness', 'Ripeness', 'Acidity']