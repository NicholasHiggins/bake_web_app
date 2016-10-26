from django.contrib import admin

from .models import Ingredient, Formula, Ratio, SoakerRatio

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

# Register your models here.
