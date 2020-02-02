from django import forms

from .models import Inicjator
from django.core.validators import RegexValidator

class InicjatorForm(forms.ModelForm):
    my_validator = RegexValidator("^[1-9]{6}\@student\.pwr\.edu\.pl|([a-zA-Z])\.[a-zA-Z]*\@pwr\.edu\.pl", "Insert university email")
    email = forms.EmailField(label="Email*", validators=[my_validator]	)
    imie = forms.CharField(label="Imię*")
    nazwisko = forms.CharField(label="Nazwisko*")
    haslo = forms.CharField(label="Hasło*", widget = forms.TextInput(attrs={"type":"password"}))
    class Meta:
        model = Inicjator
        fields =[
			'rola', 
			'email',	
			'imie',
			'nazwisko',
			'haslo'
		]