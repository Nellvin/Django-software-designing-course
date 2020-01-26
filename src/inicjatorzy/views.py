from django.shortcuts import render

from .models import Inicjator
from .forms import InicjatorForm

def inicjator_create_view(request):
	label = False
	form = InicjatorForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = InicjatorForm()
		label = True

	context={
		"form" : form,
		"label" : label
	}
	return render(request, "inicjatorzy/inicjator_create.html",context) 