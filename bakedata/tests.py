from django.test import TestCase
from .models import Ingredient, Formula, Ratio


class ModelsTestCase(TestCase):
	def setUp(self):
		i1=Ingredient.objects.create(name='ingredientONE',
							 amount=1234.56)
		i2=Ingredient.objects.create(name='ingredientTWO',amount=2222.22)
		f1=Formula.objects.create(name='formulaONE')
		f2=Formula.objects.create(name='formulaTWO')		
		r1=Ratio.objects.create(formula=f1,
						ingredient=i1, ratio=100)
		r2=Ratio.objects.create(formula=f1,
						ingredient=i2, ratio=65)

	def test_Ratio_ensures_no_duplicate_formula-ingredient_ratios(self):
		r3=Ratio.objects.creat(formula=f1,ingredient=i2, ratio=64)

	def test_can_create_ingredient(self):
		t=Ingredient.objects.create(name='ingredient_name',
							 amount=1234.56)
		self.assertEqual(t.name,'ingredient_name')
		self.assertEqual(t.amount,1234.56)

	def test_can_retrieve_object_info(self):
		ingredient= Ingredient.objects.get(
						name='ingredient_name')
		self.assertEqual(ingredient.name,'ingredient_name')
:
	
	def test_create_formula(self):
		pass
	
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
		


# Create your tests here.
