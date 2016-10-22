from django.db import models


class Ingredient(models.Model):
	name=models.CharField(max_length=30)
	amount=models.DecimalField(max_digits=6,decimal_places=2)

	def __str__(self):
		return self.name

class Formula(models.Model):
	# represents the baker's percentage relationship between 
	# Ingredients. Needs to provide for special case where a 
	# soaker is used.
	name = models.CharField(max_length=60)
	ingredients = models.ManyToManyField(Ingredient, 
					through='Ratio')

	def __str__(self):
		return self.name

class Ratio(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	formula = models.ForeignKey(Formula)
	ratio = models.DecimalField(max_digits=5,decimal_places=2)

	
