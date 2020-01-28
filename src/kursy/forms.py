from django import forms

from .models import Kurs

class KursForm(forms.ModelForm):
	kodKursu = forms.CharField( label='Kod Kursu', widget=forms.TextInput(attrs={"placeholder":"Podaj kod kursu"}))
	nazwa = forms.CharField()
	liczbaECTS = forms.IntegerField(label='Liczba ECTS')
	class Meta:
		model = Kurs
		fields =[
			'kodKursu', 
			'nazwa',	
			'ECTS'
		]

class RawKursForm(forms.Form):
	kodKursu = forms.CharField( label='Kod Kursu', widget=forms.TextInput(attrs={"placeholder":"Podaj kod kursu"}))
	nazwa = forms.CharField()
	liczbaECTS = forms.IntegerField(label='Liczba ECTS')