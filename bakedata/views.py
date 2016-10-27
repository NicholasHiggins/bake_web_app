from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('This is the index page, you shitbird!')

def ingredients_menu(request):
	pass

def formulas_menu(request):
	pass


# Create your views here.
