from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Ingredient, Formula, Ratio, SoakerRatio, Load, Bake

admin.site.register(Ingredient)

class RatioInline(admin.StackedInline):
		model = Ratio
		extra = 2		

class SoakerRatioInline(admin.StackedInline):
		model = SoakerRatio
		extra = 1
	
class FormulaAdmin(admin.ModelAdmin):
		fieldsets=[
		(None,		{'fields':['name']}),
		]
		inlines= [RatioInline,SoakerRatioInline]
	
admin.site.register(Formula,FormulaAdmin)

class SoakerRatioInline(admin.StackedInline):
		model = SoakerRatio
		extra = 1

class LoadAdmin(admin.ModelAdmin):
		fieldsets=[
		(None, {'fields':('formula','loaf_mass','number_of_loaves')}),
		]

admin.site.register(Load,LoadAdmin)

class LoadsInLine(admin.TabularInline):
		model = Bake.loads.through
		extra = 0
class BakeAdmin(admin.ModelAdmin):
		inlines = [
			LoadsInLine,
			]
		exclude = ('loads',)
		actions = ['view_bake_object']
		def has_delete_permission(self, request,obj=None):
			return True

		def view_bake_object(modeladmin, request, queryset):
			return HttpResponseRedirect('/bakedata/bake/{0}/view/'.format(queryset.get().id))
		view_bake_object.short_description = 'View the bake'
		

admin.site.register(Bake,BakeAdmin)

# Register your models here.
