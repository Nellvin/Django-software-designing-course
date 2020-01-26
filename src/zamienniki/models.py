from django.db import models
from inicjatorzy.models import Inicjator
from django.db.models import Sum
from kursy.models import Kurs 

from django.utils.translation import gettext_lazy as _

# Create your models here.
class Zamiennik(models.Model):
	class Status(models.TextChoices):
		OCZEKUJACY = 'OCZEK', _('Oczekujący')
		ODRZUCONY = 'ODRZ', _('Odrzucony')
		ZAAKCEPTOWANY = 'AKCP', _('Zaakceptowany')


	statusZamiennika =models.CharField(
		max_length = 10,
		choices = Status.choices,
		default = Status.OCZEKUJACY
    	)

	inicjator = models.ForeignKey(
		Inicjator,
		on_delete = models.SET_NULL,
		blank = False,
		null = True,
    	)

	kursZamieniany = models.ForeignKey(
		Kurs,
		on_delete = models.SET_NULL,
		blank = False,
		null = True,
		related_name = 'zamiennik',
		)

	kursyZamiennika = models.ManyToManyField(
		Kurs,
		related_name = "kursyWchodząceWSkładZamiennika"
		)

	


	def zaakceptuj_zamiennik(self):
		self.statusZamiennika = 'AKCP'
		try:
			self.save()
		except:
			return False
		return True

	def odrzuc_zamiennik(self):
		self.statusZamiennika = 'ODRZ'
		try:
			self.save()
		except:
			return False
		return True

	def __str__(self):
		 # (self.kursyZamiennika.aggregate(Sum('liczbaECTS')))
		return 'zamiennik: '+self.kursZamieniany.kodKursu
		pass

	def sumaECTS(self):
		return (self.kursyZamiennika.aggregate(Sum('liczbaECTS'))['liczbaECTS__sum'])

	def getFormaZaliczenia(self):
		return self.kursyZamiennika.first().get_formaZaliczenia_display()

	def getZZU(self):
		return (self.kursyZamiennika.aggregate(Sum('liczbaGodzin'))['liczbaGodzin__sum'])

	def getFormaZajec(self):
		liczbaFormZajęć = self.kursyZamiennika.values('formaZajec').distinct()
		if(liczbaFormZajęć.count()>1):
			return "grupa kursów"
		else:
			return self.kursyZamiennika.first().get_formaZajec_display()
		
		pass

	def getStopienStudiow(self):
		s = self.kursyZamiennika.first().planstudiow.get_stpienStudiow_display()
		return s
    # class FormaZaliczenia(models.TextChoices):
    #     EGZAMIN = 'EG', _('Egzamin')
    #     ZALICZENIE_NA_OCENE = 'ZNO', _('Zaliczenie na ocenę')

    # class FormaZajec(models.TextChoices):
    # 	WYKLAD = 'WYK', _('Wykład')
    # 	LABORATORIUM = 'LAB', _('Laboratorium')
    # 	SEMINARIUM = 'SEM', _('Seminarium')
    # 	PROJEKT = 'PROJ', _('Projekt')
    # 	CWIECZENIE = 'CW', _('Ćwiczenie')


    


    # kodKursu = models.CharField(
    # 	max_length = 8
    # 	)
    # nazwa = models.TextField()
    # liczbaECTS = models.PositiveSmallIntegerField(
    # 	blank=False, 
    # 	null=False
    # 	)
    # formaZaliczenia = models.CharField(
    # 	max_length = 20, 
    # 	choices=FormaZaliczenia.choices,
    # 	default=FormaZaliczenia.ZALICZENIE_NA_OCENE
    # 	)
    # formaZajec = models.CharField(
    # 	max_length = 20,
    # 	choices = FormaZajec.choices,
    # 	default = FormaZajec.WYKLAD
    # 	)
    # liczbaGodzin = models.PositiveSmallIntegerField(
    # 	blank=False, 
    # 	null=False
    # 	)
    # kartaKursu =  models.CharField(
    # 	max_length = 80, 
    # 	default = ''
    # 	)
    # slowaKluczowe = models.CharField(
    # 	max_length = 80
    # 	)
