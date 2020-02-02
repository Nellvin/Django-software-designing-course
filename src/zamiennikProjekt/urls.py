"""zamiennikProjekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view
from zamienniki.views import pdf_view, list_zamienniki, zamiennik_szczegoly
from inicjatorzy.views import inicjator_create_view

urlpatterns = [
	path('', home_view, name ='home'),
    path('createinicjator/', inicjator_create_view, name="create_inicjator"),
    path('admin/', admin.site.urls),
    path('zamienniki/',list_zamienniki, name="lista_zamiennikow"),
    path('zamiennik/<int:id>/', zamiennik_szczegoly, name='zamiennik_detail'),
    path('zamiennik/<int:id>/pdf/',pdf_view, name="pdf"),
]
