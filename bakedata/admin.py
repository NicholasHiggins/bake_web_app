from django.contrib import admin

from .models import Ingredient, Formula, Ratio, SoakerRatio, Load

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

# Register your models here.
