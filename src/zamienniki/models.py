from django.db import models
from inicjatorzy.models import Inicjator

# Create your models here.
class Zamiennik(models.Model):
	kodKursu = models.CharField(max_length = 8)
	nazwa = models.TextField()
	liczbaECTS = models.PositiveSmallIntegerField(blank=True, null=True)
	formaZaliczenia = models.CharField(max_length = 80)
	liczbaGodzin = models.PositiveSmallIntegerField(blank=True, null=True)
	formaKursu = models.CharField(max_length = 15)
	kartaKursu =  models.CharField(max_length = 80, default = '')
	slowaKluczowe = models.CharField(max_length = 80)
	statusZamiennika =models.CharField(max_length = 10)

	inicjator = models.ForeignKey(Inicjator,on_delete=models.SET_NULL,blank=True,
    null=True,)
