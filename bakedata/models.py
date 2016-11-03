from django.db import models


class Ingredient(models.Model):
	name=models.CharField(max_length=30)
	amount=models.FloatField(null=True,blank=True)

	def __str__(self):
		return self.name

	def debit(self,value):
		self.amount = round(self.amount-value,2)
		self.save(update_fields=['amount'])

	class Meta:
		ordering = ['-name']
		

class Formula(models.Model):
	# represents the baker's percentage relationship between 
	# Ingredients. Needs to provide for special case where a 
	# soaker is used.
	name = models.CharField(max_length=60)
	soaker_percent = models.IntegerField(default=0)
	ingredients = models.ManyToManyField(Ingredient, 
					through='Ratio',related_name='Ratio') 
	soaker = models.ManyToManyField(Ingredient, through=
					'SoakerRatio',related_name='SoakerRatio')

	def __str__(self):
		return self.name

	def total_percent(self):
		p=float(self.soaker_percent)
		for item in Ratio.objects.filter(
						formula__exact=self):
			p+=float(item.ratio)
		return p

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

class Load(models.Model):
	formula = models.ForeignKey(Formula)
	loaf_mass = models.DecimalField(
					max_digits=6,decimal_places=3)
	number_of_loaves = models.IntegerField()
	
	
	def total_mass(self):
		return float(self.loaf_mass*self.number_of_loaves)

	def recipe_calc(self):
	# returns a dictionary with formula ingredient keys and 
	# calculated values. This will be displayed in views.
		k=float(self.total_mass()/self.formula.total_percent())
		T={}
		for item in Ratio.objects.filter(
						formula__exact=self.formula):
			T[item.ingredient.name]=round(k*float(item.ratio),3)
		soaker_sum_percent=0
		for item in SoakerRatio.objects.filter( 
						formula__exact=self.formula):
			soaker_sum_percent+=item.ratio # get total soaker percent
		for item in SoakerRatio.objects.filter(
						formula__exact=self.formula):
			s='Soaker '+item.ingredient.name # find percent of total for item
			T[s]=round(k*float(item.ratio/soaker_sum_percent)*float(
							self.formula.soaker_percent),3)		
		return T	
	recipe = property(recipe_calc)	

	def __str__(self):
		return '{0} Loaves of {2} ({1} g)'.format(self.number_of_loaves,
							int(self.loaf_mass*1000),self.formula.name)
	def name(self):
		# Is this even used?
		return str(self)

	def print_load(self):
		for name in self.recipe:
			print('{0:<20} {1:>12}'.format(name,self.recipe[name]))
	readout=property(print_load)


class Bake(models.Model):
	loads = models.ManyToManyField(Load)
	date_of_bake = models.DateTimeField()
	name = models.CharField(max_length=30)


	def debit_ingredients(self):
		for load in self.loads.all():
			K=load.recipe
			for item in K:			
				s=Ingredient.objects.get(name__exact=item)				
				s.debit(K[item])

	def __str__(self):
		return '{0} {1}'.format(self.name,self.date_of_bake.strftime('%A %b %d at %H:%M'))

	def amount_needed(self,ingredient):
		amount_needed=0
		for load in self.loads.all():
			K=load.recipe
			if ingredient.name in K:
				amount_needed+=K[ingredient.name]
		return amount_needed	

	
