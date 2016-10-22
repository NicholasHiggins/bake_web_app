from django.contrib import admin

from .models import Ingredient, Formula, Ratio

admin.site.register(Ingredient)

class RatioInline(admin.StackedInline):
		model = Ratio
		extra = 2		
		
class FormulaAdmin(admin.ModelAdmin):
		fieldsets=[
		(None,		{'fields':['name']}),
		]
		inlines= [RatioInline]
	


admin.site.register(Formula,FormulaAdmin)


# Register your models here.
