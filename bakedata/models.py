from django.db import models


class Ingredient(models.Model):
	name=models.CharField(max_length=30)
	amount=models.FloatField()

	def __str__(self):
		return self.name

	def debit(self,value):
		self.amount = round(self.amount-value,2)
		self.save(update_fields=['amount'])
		

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
			T[item.ingredient.name]=k*float(item.ratio)
		for item in SoakerRatio.objects.filter(
						formula__exact=self.formula):
			s='soaker'+item.ingredient.name
			T[s]=k*float(item.ratio)*float(self.soaker_percent)/100		
		return T	
	recipe = property(recipe_calc)	

	def __str__(self):
		return '{0} Loaves of {2} ({1} g).'.format(self.number_of_loaves,
							int(self.loaf_mass*1000),self.formula.name)
	def name(self):
		return str(self)

class Bake(models.Model):
	loads = models.ManyToManyField(Load)
	date_edited = models.DateField(auto_now=True)
	name = models.CharField(max_length=30)

	def debit_ingredients(self):
		for load in self.loads.all():
			K=load.recipe()
			for item in K:			
				s=Ingredient.objects.get(name__exact=item)				
				s.debit(K[item])

	def __str__(self):
		return '{0} {1}'.format(self.name,self.date_edited)
				

	
