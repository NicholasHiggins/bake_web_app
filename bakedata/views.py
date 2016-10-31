from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Load, Bake

def index(request):
	load_list_=Load.objects.all()
	return render(request, 'index.html', {'load_list': load_list_})

def ingredients_menu(request):
	pass

def formulas_menu(request):
	pass

def view_bake(request,bake_id):
	# Because we can't call a function in template, we must detail the 
	# recipe relationship within loads of bake as a tuple of 2-tuples
	# UNTIDY BAD SMELL FIX THIS! - have to change how load.recipe 
	# stored in db.
	bake=get_object_or_404(Bake,pk=bake_id)
	loads=bake.loads.all()
	return render(request, 'view_bake.html', {'bake': bake,'loads':loads})

# Create your views here.
