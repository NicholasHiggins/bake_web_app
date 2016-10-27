from django.test import TestCase
from .models import *


class ModelsTestCase(TestCase):
	def setUp(self):
		self.i1=Ingredient.objects.create(name='ingredientONE',
					amount=1234.56)
		self.i2=Ingredient.objects.create(
					name='ingredientTWO',amount=2222.22)	
		self.f1=Formula.objects.create(name='formulaONE')		
		self.f2=Formula.objects.create(name='formulaTWO')	
		self.r1=Ratio.objects.create(formula=self.f1,
						ingredient=self.i1, ratio=100)		
		self.r2=Ratio.objects.create(formula=self.f1,
						ingredient=self.i2, ratio=100)
		self.l1=Load(formula=self.f1, loaf_mass=1,
				number_of_loaves = 2)


	def test_no_duplicate_formula_ingredient_ratios(self):
		f1=Formula.objects.create(name='formulaONE')
		i1=Ingredient.objects.create(name='ingredientONE',
					amount=1234.56)
		r1=Ratio.objects.create(formula=f1,
						ingredient=i1, ratio=100)		
		try:
			r2=Ratio.objects.create(formula=f1,ingredient=i1,
					 ratio=64)
		except: 
			pass
		
		else:
			self.fail('allowed for non-unique ratio 						entries')		

	def test_can_create_ingredient(self):
		i1=Ingredient.objects.create(name='ingredientONE',
					amount=1234.56)
		i2=Ingredient.objects.create(
					name='ingredientTWO',amount=2222.22)

		self.assertEqual(i1.name,'ingredientONE')
		self.assertEqual(i1.amount,1234.56)
		self.assertEqual(i2.name,'ingredientTWO')
		self.assertEqual(i2.amount,2222.22)

	def test_can_retrieve_object_info(self):
		ingredient= Ingredient.objects.get(
						name='ingredientONE')

		self.assertEqual(ingredient.name,'ingredientONE')

	
	def test_can_create_formula(self):
		f1=Formula.objects.create(name='formulaONE')		
		f2=Formula.objects.create(name='formulaTWO')	
		
		self.assertEqual(f1.name,'formulaONE')
		self.assertEqual(f2.name,'formulaTWO')
	
	def test_ratio_works(self):
		i1=Ingredient.objects.create(
						name='White',amount=100.00)
		i2=Ingredient.objects.create(
						name='Water',amount=300.00)
		f1=Formula.objects.create(name='White Sourdough')
		r1=Ratio.objects.create(formula=f1,
						ingredient=i1, ratio=100)
		self.assertEqual(100,r1.ratio)

	def test_formula_has_a_soaker(self):
	#	i1=Ingredient.objects.create(
	#					name='White',amount=100.00)		
	#	f1=Formula.objects.create(name='formulaONE')
		self.assertTrue(self.f1.soaker)
		sr1=SoakerRatio.objects.create(
					formula=self.f1,ingredient=self.i1,ratio=65)
		self.assertNotEqual(self.f1.soaker,'')
		
	def test_formula_method_total_percent(self):
		t=self.f1.total_percent()
		self.assertEqual(t,200)

	def test_Load_method_total_mass(self):
		self.assertEqual(self.l1.total_mass(),2.0)

	def test_Load_method_recipe(self):
		K=self.l1.recipe()
		self.assertEqual(K[self.i1.name],1)
		self.assertEqual(K[self.i2.name],1)

