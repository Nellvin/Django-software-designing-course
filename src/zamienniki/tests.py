from django.test import TestCase
from zamienniki.models import Zamiennik
from kursy.models import Kurs

# Create your tests here.
class TestModels(TestCase):
	# Given
	def setUp(self):
		self.zamiennik1 = Zamiennik.objects.create(
			statusZamiennika='OCZEK'
			)

	def test_zaakaceptuj_zamiennik(self):
		
		self.zamiennik1.zaakceptuj_zamiennik()
		self.assertEquals(self.zamiennik1.statusZamiennika, 'AKCP')

	def test_odrzuc_zamiennik(self):
		
		self.zamiennik1.odrzuc_zamiennik()
		self.assertEquals(self.zamiennik1.statusZamiennika, 'ODRZ')

	def test_sumy_ectsow(self):
		
		kurs1 = Kurs.objects.create(
			liczbaECTS = 5,
			liczbaGodzin =15)
		kurs2 = Kurs.objects.create(
			liczbaECTS = 3,
			liczbaGodzin =15)
		self.zamiennik1.kursyZamiennika.add(kurs1)
		self.zamiennik1.kursyZamiennika.add(kurs2)
		self.assertEquals(self.zamiennik1.sumaECTS(),8)

	def test_ZZU(self):
		self.assertEquals(self.zamiennik1.getZZU(),0)
		kurs1 = Kurs.objects.create(
			liczbaECTS = 5,
			liczbaGodzin =15)
		kurs2 = Kurs.objects.create(
			liczbaECTS = 3,
			liczbaGodzin =30)
		self.zamiennik1.kursyZamiennika.add(kurs1)
		self.zamiennik1.kursyZamiennika.add(kurs2)
		self.assertEquals(self.zamiennik1.getZZU(),45)
