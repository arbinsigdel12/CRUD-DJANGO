from django import forms
from .models import *

class AddEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields =("name","roll","city")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }