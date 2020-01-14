from django.shortcuts import render

from .models import Kurs
from .forms import KursForm, RawKursForm
# Create your views here.

def kurs_create_view(request):
	form = KursForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = KursForm()
	context={
		"form" : form
	}
	return render(request, "kursy/kurs_create.html",context) 

# def kurs_create_view(request):
# 	if request.method=="POST":
# 		new_kod=request.POST.get('nameKurs')
# 		print(new_kod)
# 	context={
# 	}
# 	return render(request, "kursy/kurs_create.html",context) 


# def kurs_create_view(request):
# 	form = KursForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = KursForm()
# 	context={
# 		'form': form
# 	}
# 	return render(request, "kursy/kurs_create.html",context) 

def kurs_detail_view(request):
	obj = Kurs.objects.get(id=1)
	context={
		'kodK': obj.kodKursu
	}
	return render(request, "kursy/kurs_detail.html" ,context) 
