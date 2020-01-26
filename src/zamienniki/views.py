from django.shortcuts import render
from django.http import FileResponse, Http404
from django.db.models import Sum

from .models import Zamiennik
def pdf_view(request):
    # try:
        return FileResponse(open('C:/Users/Filip/Documents/Studia 2019-2020/PO/Project/myenv/src/zamienniki/W08_20.pdf', 'rb'), content_type='application/pdf')
    # except FileNotFoundError:
    #     raise Http404()

def list_zamienniki(request):
    
    query_set = Zamiennik.objects.filter(statusZamiennika='OCZEK')
    context = {
        "obj_list" : query_set
    }
    return render(request, "zamienniki/list_zamienniki.html",context)

def zamiennik_szczegoly(request,id):
    instance = Zamiennik.objects.get(id=id)
    if 'oczek' in request.POST:
    	instance.statusZamiennika= 'OCZEK'
    	instance.save()
    if 'odrz' in request.POST:
    	instance.statusZamiennika= 'ODRZ'
    	instance.save()
    if 'akcept' in request.POST:
    	instance.statusZamiennika= 'AKCP'
    	instance.save()

    nazwaK = instance.kursZamieniany.nazwa
    kodK = instance.kursZamieniany.kodKursu
    imieI = instance.inicjator.imie
    nazwiskoI = instance.inicjator.nazwisko
    ECTS = instance.sumaECTS()
    zaliczenie = instance.getFormaZaliczenia()
    stopien = instance.getStopienStudiow()
    ZZU = instance.getZZU()
    formaZajec = instance.getFormaZajec()
    status = instance.get_statusZamiennika_display()
    setKursowZamiennika = instance.kursyZamiennika.all()
    context = {
    	"instance": instance,
        "nazwaK" : nazwaK,
        "kodK" : kodK,
        "imieI" : imieI,
        "nazwiskoI" : nazwiskoI,
        "ECTS" : ECTS,
        "zaliczenie" : zaliczenie,
        "stopien" : stopien,
        "ZZU" : ZZU,
        "formaZajec" : formaZajec,
        "status": status,
        "setKursowZamiennika" : setKursowZamiennika,
        "id" : str("0000000"+str(instance.id)) 
    }
    return render(request, "zamienniki/zamiennik_details.html",context)

