from django.test import TestCase
from .models import Ingredient, Formula, Ratio


class ModelsTestCase(TestCase):
	def setUp(self):
		i1=Ingredient.objects.create(name='ingredientONE',
					amount=1234.56)
		i2=Ingredient.objects.create(
					name='ingredientTWO',amount=2222.22)	
		f1=Formula.objects.create(name='formulaONE')		
		f2=Formula.objects.create(name='formulaTWO')	
		r1=Ratio.objects.create(formula=f1,
						ingredient=i1, ratio=100)		
		r2=Ratio.objects.create(formula=f1,
						ingredient=i2, ratio=65)


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
		
