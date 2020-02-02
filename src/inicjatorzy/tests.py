from django.test import TestCase
from inicjatorzy.models import Inicjator
# Create your tests here.

class TestModels(TestCase):

	def setUp(self):
		self.inicjator1 = Inicjator(
			email = '242541@student.pwr.edu.pl',
			rola = 'ST'
			)
		self.inicjator2 = Inicjator(
			rola = 'ST'
			)
		self.inicjator3 = Inicjator(
			email = 'abcded@student.pwr.edu.pl',
			)

	def test_ustaw_indeks_bez_maila(self):
		self.assertEquals(self.inicjator2.indeks, None)
		self.assertEquals(self.inicjator2.extract_indeks(), '')

	def test_ustaw_indeks(self):
		self.assertEquals(self.inicjator1.indeks, None)
		self.assertEquals(self.inicjator1.extract_indeks(), '242541')

	def test_ustaw_indeks_błedny(self):
		self.assertEquals(self.inicjator3.indeks, None)
		self.assertEquals(self.inicjator3.extract_indeks(), '')

	def test_czy_liczba(self):
		self.assertEquals(self.inicjator1.isNum('555'), True)
		self.assertEquals(self.inicjator1.isNum('55a5'), False)