from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Inicjator(models.Model):
    class Role(models.TextChoices):
        STUDENT = 'ST', _('Student')
        OSOBA_OPINIUJACA = 'OO', _('Osoba Opiniująca')

    imie = models.CharField(max_length = 30)
    nazwisko = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    haslo = models.CharField(max_length = 500)
    indeks = models.PositiveSmallIntegerField(null = True)

    rola = models.CharField(
		max_length = 20, 
		choices=Role.choices ,
        default=Role.STUDENT,
	)