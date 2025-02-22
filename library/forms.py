from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['user']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating >= 5:
            raise forms.ValidationError('You can rate upto 5.')
        return rating
