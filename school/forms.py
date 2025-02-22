from django import forms
from .models import Numerical


class NumericalForm(forms.ModelForm):
    class Meta:
        model = Numerical
        fields = '__all__'
