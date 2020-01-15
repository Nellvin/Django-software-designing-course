from django.db import models
from inicjatorzy.models import Inicjator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Zamiennik(models.Model):
    class FormaZaliczenia(models.TextChoices):
        EGZAMIN = 'EG', _('Egzamin')
        ZALICZENIE_NA_OCENE = 'ZNO', _('Zaliczenie na ocenę')

    class FormaZajec(models.TextChoices):
    	WYKLAD = 'WYK', _('Wykład')
    	LABORATORIUM = 'LAB', _('Laboratorium')
    	SEMINARIUM = 'SEM', _('Seminarium')
    	PROJEKT = 'PROJ', _('Projekt')
    	CWIECZENIE = 'CW', _('Ćwiczenie')


    class Status(models.TextChoices):
    	OCZEKUJACY = 'OCZEK', _('Oczekujący')
    	ODRZUCONY = 'ODRZ', _('Odrzucony')
    	ZAAKCEPTOWANY = 'AKCP', _('Zaakceptowany')


    kodKursu = models.CharField(
    	max_length = 8
    	)
    nazwa = models.TextField()
    liczbaECTS = models.PositiveSmallIntegerField(
    	blank=False, 
    	null=False
    	)
    formaZaliczenia = models.CharField(
    	max_length = 20, 
    	choices=FormaZaliczenia.choices,
    	default=FormaZaliczenia.ZALICZENIE_NA_OCENE
    	)
    formaZajec = models.CharField(
    	max_length = 20,
    	choices = FormaZajec.choices,
    	default = FormaZajec.WYKLAD
    	)
    liczbaGodzin = models.PositiveSmallIntegerField(
    	blank=False, 
    	null=False
    	)
    kartaKursu =  models.CharField(
    	max_length = 80, 
    	default = ''
    	)
    slowaKluczowe = models.CharField(
    	max_length = 80
    	)
    statusZamiennika =models.CharField(
    	max_length = 10,
    	choices = Status.choices,
    	default = Status.OCZEKUJACY
    	)

    inicjator = models.ForeignKey(
    	Inicjator,
    	on_delete=models.SET_NULL,
    	blank=True,
    	null=True,
    	)

 #    rola = models.CharField(
	# 	max_length = 20, 
	# 	choices=Role.choices ,
 #        default=Role.STUDENT,
	# )
