from django.http import FileResponse, Http404
from django.shortcuts import render
from django.db.models import Sum

from .models import Zamiennik

def pdf_view(request, id):
    zamienniki = Zamiennik.objects.get(id=id)
    ID=str("0000000"+str(id)) 
    file1 = zamienniki.kursZamieniany.kartaKursu
    file2 = zamienniki.kursyZamiennika.first().kartaKursu
    context = {
        "file1" : file1,
        "file2" : file2,
        "id" : ID
    }
    return render(request, "pdf.html", context)

def list_zamienniki(request):
    
    query_set = Zamiennik.objects.filter(statusZamiennika='OCZEK')
    context = {
        "obj_list" : query_set
    }
    return render(request, "list_zamienniki.html",context)

def zamiennik_szczegoly(request,id):
    instance = Zamiennik.objects.get(id=id)
    if 'oczek' in request.POST:
    	instance.statusZamiennika= 'OCZEK'
    	instance.save()
    if 'odrz' in request.POST:
    	instance.odrzuc_zamiennik()
    	instance.save()
    if 'akcept' in request.POST:
    	instance.zaakceptuj_zamiennik()
    	instance.save()

    nazwaK = instance.kursZamieniany.nazwa
    kodK = instance.kursZamieniany.kodKursu
    imieI = instance.inicjator.imie
    nazwiskoI = instance.inicjator.nazwisko
    indeksI = instance.inicjator.indeks
    ECTS = instance.kursZamieniany.ECTS
    sumECTS = instance.sumaECTS()
    zaliczenie = instance.getFormaZaliczenia()
    stopien = instance.kursZamieniany.planstudiow.get_stpienStudiow_display()
    ZZU = instance.kursZamieniany.liczbaGodzin
    ZZUZamiennikow = instance.getZZU()
    formaZajec = instance.kursZamieniany.get_formaZajec_display()
    formaZajecZamiennikow = instance.getFormaZajec()
    status = instance.get_statusZamiennika_display()
    setKursowZamiennika = instance.kursyZamiennika.all()

    context = {
    	"instance": instance,
        "nazwaK" : nazwaK,
        "kodK" : kodK,
        "imieI" : imieI,
        "nazwiskoI" : nazwiskoI,
        "indeksI" : indeksI,
        "ECTS" : ECTS,
        "sumECTS" : sumECTS,
        "zaliczenie" : zaliczenie,
        "stopien" : stopien,
        "ZZU" : ZZU,
        "ZZUZamiennikow" : ZZUZamiennikow,
        "formaZajec" : formaZajec,
        "status": status,
        "setKursowZamiennika" : setKursowZamiennika,
        "id" : str("0000000"+str(instance.id)) 
    }
    return render(request, "zamiennik_details.html",context)

