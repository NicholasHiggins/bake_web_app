from django.shortcuts import render
from django.http import HttpResponse

from .models import Load

def index(request):
	load_list_=Load.objects.all()
	return render(request, 'index.html', {'load_list': load_list_})

def ingredients_menu(request):
	pass

def formulas_menu(request):
	pass


# Create your views here.
