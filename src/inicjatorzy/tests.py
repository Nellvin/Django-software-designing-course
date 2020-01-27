from django.test import TestCase
from inicjatorzy.models import Inicjator
# Create your tests here.

class TestModels(TestCase):

	def setUp(self):
		self.inicjator1 = Inicjator(
			email = '242541@student.pwr.edu.pl',
			rola = 'ST'
			)

	def test_ustaw_indeks(self):
		self.assertEquals(self.inicjator1.indeks, None)
		self.assertEquals(self.inicjator1.extract_indeks(), '242541')

	def test_czy_liczba(self):
		self.assertEquals(self.inicjator1.isNum('555'), True)
		self.assertNotEquals(self.inicjator1.isNum('55a5'), True)