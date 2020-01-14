from django import forms

from .models import Inicjator

class InicjatorForm(forms.ModelForm):
	# kodKursu = forms.CharField( label='Kod Kursu', widget=forms.TextInput(attrs={"placeholder":"Podaj kod kursu"}))
	# nazwa = forms.CharField()
	# liczbaECTS = forms.IntegerField(label='Liczba ECTS')
	# imie = models.CharField(max_length = 30)
 #    nazwisko = models.CharField(max_length = 50)
 #    email = models.CharField(max_length = 50)
 #    haslo = models.CharField(max_length = 500)
 #    indeks = models.PositiveSmallIntegerField()

    rola = forms.ChoiceField(label="Rola")
    email = forms.EmailField(label="Email")
    imie = forms.CharField(label="Imię")
    nazwisko = forms.CharField(label="Nazwisko")
    haslo = forms.CharField(label="Hasło", widget = forms.TextInput(attrs={"type":"password"}))
    class Meta:
        model = Inicjator
        fields =[
			'rola', 
			'email',	
			'imie',
			'nazwisko',
			'haslo'
		]