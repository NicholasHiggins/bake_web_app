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
					through='Ratio',related_name='Ratio') 
	soaker = models.ManyToManyField(Ingredient, through=
					'SoakerRatio',related_name='SoakerRatio')
	def __str__(self):
		return self.name

class Ratio(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	formula = models.ForeignKey(Formula)
	ratio = models.DecimalField(max_digits=5,decimal_places=2)
	
	
	def __str__(self):
				
		return ('{0:<20} in {1:>20}'.format(
					self.ingredient.name,self.formula.name))
	
	class Meta:
		unique_together=('ingredient','formula')

class SoakerRatio(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	formula = models.ForeignKey(Formula)
	ratio = models.DecimalField(max_digits=5,decimal_places=2)
	
	
	def __str__(self):
				
		return ('{0:<20} in {1:>20}'.format(
					self.ingredient.name,self.formula.name))
	
	class Meta:
		unique_together=('ingredient','formula')


"""
class Load(models.Model):
	formula = models.ForeignKey(Formula)
	loaf_mass = models.DecimalField(
					max_digits=6,decimal_places=3)
	number_of_loaves = models.IntegerField()
	#recipe = 
"""
#class Recipe:
	# recipe is similar to ration take many to many of Load and Ingredient
	# returns a calculated amount based on load.formula and ingredient.
	
