"""
Komenarz modułu
"""
from django.db import models
from inicjatorzy.models import Inicjator
from django.db.models import Sum
from kursy.models import Kurs 
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Zamiennik(models.Model):
	"""
	Klasa ta reprezentuje zamiennik

	Obiekty tej klasy będą rozpatrywane jako propozycje zamienników kursów na studiach.
	Przy tworzeniu automatycznie ich status jest ustawiany na *Oczekujący*

	:param statusZamiennika: reprezentuje w jakim momencie rozpatrywania znajduje sie zamiennik
	:type statusZamiennika: enum:'Status'
	:param inicjator: osoba, która zaproponowała dany zamiennik
	:type inicjator: class:'Inicjator'
	:param kursZamieniany: kurs jaki zamiennik ma zamieniać 
	:type kursZamieniany: class:'Kurs'
	:param kursyZamiennika: kursy, które które wchodzą w skład zamiennika
	:type kursyZamiennika: list of class :'Kurs'
	"""
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
		sum = self.kursyZamiennika.aggregate(Sum('liczbaECTS'))['liczbaECTS__sum']
		if(sum == None):
			return 0
		return (sum)

	def getFormaZaliczenia(self):
		forma = self.kursyZamiennika.first().get_formaZaliczenia_display()
		if (forma == None):
			return ""
		return forma

	def getZZU(self):
		ZZU = self.kursyZamiennika.aggregate(Sum('liczbaGodzin'))['liczbaGodzin__sum']
		if(ZZU == None):
			return 0
		return (ZZU)

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
