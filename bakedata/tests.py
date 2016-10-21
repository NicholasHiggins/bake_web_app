from django.test import TestCase
from .models import Ingredient, Formula, Ratio


class IngredientTestCase(TestCase):
	def setUp(self):
		t=Ingredient.objects.create(name='ingredient_name',
							 stock_amount=1234.56)

	def test_can_create_ingredient(self):
		t=Ingredient.objects.create(name='ingredient_name',
							 stock_amount=1234.56)
		self.assertEqual(t.name,'ingredient_name')
		self.assertEqual(t.stock_amount,1234.56)

	def test_can_retrieve_object_info(self):
		ingredient= Ingredient.objects.get(name='ingredient_name')
		self.assertEqual(ingredient.name,'ingredient_name')

class FormulaTestCase(TestCase):
	
	def test_create_formula(self):
		pass

class RatioTestCase(TestCase):
	
	def test_ratio_works(self):
		i1=Ingredient.objects.create(name='White',stock_amount=100.00)
		i2=Ingredient.objects.create(name='Water',stock_amount=300.00)
		f1=Formula.objects.create(name='White Sourdough')
		r1=Ratio.objects.create(formula=f1, ingredient=i1, ratio=100)
		r1.save()
		self.assertEqual(100,r1.ratio)

# Create your tests here.
