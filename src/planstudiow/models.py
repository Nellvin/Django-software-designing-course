from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class PlanStudiow(models.Model):
    class Stopien(models.TextChoices):
        PIERWSZY = 'P', _('I')
        DRUGI = 'D', _('II')

    class FormaS(models.TextChoices):
        STACJONARNE = 'S', _('Stacjonarne')
        NIESTACJONARNE = 'NS', _('Niestacjonarne')

    stpienStudiow = models.CharField(
        max_length = 20, 
        choices=Stopien.choices ,
        default=Stopien.PIERWSZY,
    )
    formaStudiow = models.CharField(
        max_length = 20, 
        choices=FormaS.choices ,
        default=FormaS.STACJONARNE,
    )
    
    liczbaSemestrow = models.PositiveIntegerField() 
    jezykStudiow = models.CharField(max_length = 30)
    specjalnosc = models.CharField(max_length = 30)
    obowiazujeOd = models.DateField()  

    def __str__(self):
    	return 'Plan : ' + str(self.id) 