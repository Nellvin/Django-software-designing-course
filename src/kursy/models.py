from django.db import models

# Create your models here.
class Kurs(models.Model):
	kodKursu = models.CharField(max_length = 8)
	nazwa = models.TextField()
	liczbaECTS = models.PositiveSmallIntegerField(blank=True, null=True)
	formaZaliczenia = models.CharField(max_length = 80)
	liczbaGodzin = models.PositiveSmallIntegerField(blank=True, null=True)
	formaKursu = models.CharField(max_length = 15)
	kartaKursu =  models.CharField(max_length = 80)
	