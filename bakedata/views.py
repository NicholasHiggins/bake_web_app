from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import datetime

from .models import Load, Bake, Ingredient, Formula

def index(request):
	load_list_=Load.objects.all()
	return render(request, 'index.html', {'load_list': load_list_})

def ingredients_menu(request):
	pass

def formulas_menu(request):
	pass

def view_bake(request,bake_id):
	bake=get_object_or_404(Bake,pk=bake_id)
	loads=bake.loads.all()
	return render(request, 'view_bake.html', {'bake': bake,'loads':loads})

def bake_data(request,bake_id):
	# will display the ingredients required for the bake, number of loaves
	# produced, total mass of dough.
	pass

def leaven_schedule(request,bake_id):
	# getting a hold on all the required objects	
	bake = get_object_or_404(Bake, pk = bake_id)	
	leaven = get_object_or_404(Ingredient, name__exact = 'Leaven')
	build = get_object_or_404(Formula, name__exact = 'Leaven Build')
	revive = get_object_or_404(Formula, name__exact = 'Leaven Revive')
	refresh = get_object_or_404(Formula, name__exact = 'Leaven Refresh')
	store = get_object_or_404(Formula, name__exact = 'Leaven Store')
	# now can calculate the different builds as loads	
	req_leaven= 1.07*(bake.amount_needed(leaven))
	d12=Load(formula = build, loaf_mass = req_leaven, number_of_loaves = 1,)
	# calculate the new req_leaven to build d12
	req_leaven = 1.07*(d12.recipe['Leaven'])
	if req_leaven < 0.370:
		req_leaven=0.370
	# create the loads for the leaven stages in order to get the readout to display in view
	d24=Load(formula = refresh, loaf_mass = req_leaven, number_of_loaves = 1)
	d36=Load(formula = refresh, loaf_mass = 0.370, number_of_loaves = 1)
	d48=Load(formula = refresh, loaf_mass = 0.370, number_of_loaves = 1)
	d60=Load(formula = revive, loaf_mass = 0.475, number_of_loaves = 1)
	# define time's for builds	
	time_delta=datetime.timedelta(hours=-12)
	t_time=bake.date_of_bake
	t_12=t_time-time_delta
	t_12=t_12.strftime('%A %b %d at %H:%M') #convert to string for template
	t_24=t_time-2*time_delta
	t_24=t_24.strftime('%A %b %d at %H:%M')
	t_36=t_time-3*time_delta
	t_36=t_36.strftime('%A %b %d at %H:%M')
	t_48=t_time-4*time_delta
	t_48=t_48.strftime('%A %b %d at %H:%M')	
	t_60=t_time-5*time_delta
	t_60=t_60.strftime('%A %b %d at %H:%M')
	t_time=t_time.strftime('%A %b %d at %H:%M')
	loads=[(d60,t_60),(d48,t_48),(d36,t_36),(d24,t_24),(d12,t_12)] 
	# clean up, we're finished with these loads	
	# actually don't know if we can delete these loads, best to perhaps
	# just keep them hidden in admin. Turns out they don't show up in admin
	# probably because I never call the save function. hmmmm
#	d12.delete()
#	d24.delete()
#	d36.delete()
#	d48.delete()
#	d60.delete()
	context = { 'loads': loads, 'bake': bake,
				}
	# now send to html
	return render(request, 'leaven_schedule.html', context)	
# will produce and display the leaven schedule for a particular bake
	pass
# Create your views here.
