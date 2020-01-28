from django.db import models
from planstudiow.models import PlanStudiow 
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Kurs(models.Model):
    class FormaZaliczenia(models.TextChoices):
        EGZAMIN = 'EG', _('Egzamin')
        ZALICZENIE_NA_OCENE = 'ZNO', _('Zaliczenie na ocenę')

    class FormaZajec(models.TextChoices):
    	WYKLAD = 'WYK', _('Wykład')
    	LABORATORIUM = 'LAB', _('Laboratorium')
    	SEMINARIUM = 'SEM', _('Seminarium')
    	PROJEKT = 'PROJ', _('Projekt')
    	CWIECZENIE = 'CW', _('Ćwiczenie')

    kodKursu = models.CharField(max_length = 15)
    nazwa = models.TextField()
    ECTS = models.PositiveSmallIntegerField(blank=False, null=False)
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
    liczbaGodzin = models.PositiveSmallIntegerField(blank=False, null=False)
    kartaKursu =  models.CharField(max_length = 80)
    planstudiow = models.ForeignKey(
		PlanStudiow,
		on_delete = models.SET_NULL,
		blank = False,
		null = True,
		)
    # plikKaraKursu = models.FileField()

    def __str__(self):
    	return self.nazwa+ ' ' + self.formaZajec[:1]

	