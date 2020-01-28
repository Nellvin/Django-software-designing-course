"""
Komenarz modułu
"""
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from django.db import models

from inicjatorzy.models import Inicjator
from kursy.models import Kurs

#pylint: disable=bad-whitespace
#pylint: disable=invalid-name

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
        """Emumerator statsu zamiennika"""
        OCZEKUJACY = 'OCZEK', _('Oczekujący')
        ODRZUCONY = 'ODRZ', _('Odrzucony')
        ZAAKCEPTOWANY = 'AKCP', _('Zaakceptowany')

    statusZamiennika = models.CharField(
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
        """Funkcja powoduje zmiane status zamiennika na status zaakceptowany"""

        self.statusZamiennika = 'AKCP'
        try:
            self.save()
        except:
            return False
        return True

    def odrzuc_zamiennik(self):
        """Funkcja powoduje zmiane status zamiennika na status odrzucony"""
        self.statusZamiennika = 'ODRZ'
        try:
            self.save()
        except:
            return False
        return True

    def __str__(self):
         # (self.kursyZamiennika.aggregate(Sum('ECTS')))
        return 'zamiennik: '+self.kursZamieniany.kodKursu


    def sumaECTS(self):
        """Funkcja zwraca sume ECTS kursów wchodzących w skład zamiennika"""
        sumECTS = self.kursyZamiennika.aggregate(Sum('ECTS'))['ECTS__sum']
        if sumECTS is None:
            return 0
        return sumECTS

    def getFormaZaliczenia(self):
        """Funkcja zwraca forme zaliczenai kursów wchodzących w skład zamiennika"""
        forma = self.kursyZamiennika.first().get_formaZaliczenia_display()
        if forma is None:
            return ""
        return forma

    def getZZU(self):
        """Funkcja zwraca sumę godzin trwania kursów wchodzących w skład zamiennika"""
        ZZU = self.kursyZamiennika.aggregate(Sum('liczbaGodzin'))['liczbaGodzin__sum']
        if ZZU is None:
            return 0
        return ZZU

    def getFormaZajec(self):
        """Funkcja zwraca forme zajęć kursów wchodzących w skład zamiennika"""
        liczbaFormZajęć = self.kursyZamiennika.values('formaZajec').distinct()
        if liczbaFormZajęć.count() > 1:
            return "grupa kursów"
        return self.kursyZamiennika.first().get_formaZajec_display()

    def getStopienStudiow(self):
        """Funkcja zwraca stopień studiów kursów wchodzących w skład zamiennika"""
        stopen_studiow = self.kursyZamiennika.first().planstudiow.get_stpienStudiow_display()
        return stopen_studiow
    