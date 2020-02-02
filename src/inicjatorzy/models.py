from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Inicjator(models.Model):
    """
        Reprezentacja osoby, która inicjuje zamiennik

        Osoba ta możę być studentem albo osobą opiniującą. Osoba opiniująca jest zdolna do zmiany 
        statusu zamiennika oraz tworznia propozycji zamiennika. Student jest zdolny jedynie do
        tworznia propozycji zamiennika  

        Attributes
        ----------
        imie : str
            imie inicjatora
        nazwisko : str
            nazwisko inicjatora
        email : str
            email uniwersytecki inicjatora
        haslo : str
            haslo inicjatora
        indeks : int
            indeks inicjatora jeżeli jest studentem

        

    """
    class Role(models.TextChoices):
        """
        Role jakie możę przyjąć inicjator
        """
        STUDENT = 'ST', _('Student')
        OSOBA_OPINIUJACA = 'OO', _('Osoba Opiniująca')

    imie = models.CharField(max_length = 30)
    nazwisko = models.CharField(max_length = 50 )
    email = models.CharField(max_length = 50, unique = True)
    haslo = models.CharField(max_length = 500)
    indeks = models.PositiveSmallIntegerField(blank = True, null = True)

    rola = models.CharField(
		max_length = 20, 
		choices=Role.choices ,
        default=Role.STUDENT,
	)

    def save(self, *args, **kwargs):
        if(self.rola == 'ST'):
            self.indeks=self.extract_indeks()
        super(Inicjator, self).save(*args, **kwargs)

    def isNum(self,data):
    	"""Funkcja sprawdza czy indeks jest """
    	try:
        	int(data)
        	return True
    	except ValueError:
        	return False

    def extract_indeks(self):
        indeks = self.email[0:6]
        if(self.isNum(indeks)):
            return indeks
        return ''

    def __str__(self):
    	return self.imie + ' ' + self.nazwisko
    	pass