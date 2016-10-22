from django.contrib import admin

from .models import Ingredient, Formula, Ratio

admin.site.register(Ingredient)
admin.site.register(Formula)
admin.site.register(Ratio)

# Register your models here.
