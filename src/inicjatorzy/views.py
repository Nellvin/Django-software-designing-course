from django.shortcuts import render

from .models import Inicjator
from .forms import InicjatorForm

def inicjator_create_view(request):
	bool_validate = False
	form = InicjatorForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = InicjatorForm()
		bool_validate = True

	context={
		"form" : form,
		"bool_validate" : bool_validate
	}
	return render(request, "inicjatorzy/inicjator_create.html",context) 