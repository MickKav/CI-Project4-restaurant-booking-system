from django import forms
from .models import Booking

class BookTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'