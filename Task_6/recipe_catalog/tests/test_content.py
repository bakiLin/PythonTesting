from django.test import TestCase, Client
from django.urls import reverse

from ..models import Ingredient, Recipe, RecipeIngredient

class TestRecipes(TestCase):
    def setUp(self):
        self.ingredient_meat = Ingredient.objects.create(name='Мясо')
        self.ingredient_potato = Ingredient.objects.create(name='Картофель')

        self.recipe = Recipe.objects.create(name='Картошка с мясом')

        self.recipe_ingredient_meat = RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient_meat, weight=100)
        self.recipe_ingredient_potato = RecipeIngredient.objects.create(recipe=self.recipe, ingredient=self.ingredient_potato, weight=200)

        self.ingredients = self.recipe.recipeingredient_set.all().order_by('ingredient__name')

        self.total_weight = 0
        for ingredient in self.ingredients:
            self.total_weight += ingredient.weight

    def test_context(self):
        """Проверка наличия всех нужных ключей в контексте"""
        url = reverse('recipe_catalog:recipe_detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)

        page_fields = (
            "title",
            "recipe_id",
            "recipe_desc",
            "ingredients",
            "total_weight"
        )

        length = sum([1 for key in page_fields if key in response.context])
        self.assertEqual(length, len(page_fields))

    def test_total_weight(self):
        """Проверка расчета суммарного веса"""
        url = reverse('recipe_catalog:recipe_detail', kwargs={'pk': self.recipe.id})
        response = self.client.get(url)
        self.assertEqual(response.context['total_weight'], self.total_weight)

    def test_recipe_detail_ingredients_order(self):
        url = reverse('recipe_catalog:recipe_detail', args=[self.recipe.id])
        response = self.client.get(url)

        ingredients = response.context['ingredients']
        names = [ingredient.ingredient.name for ingredient in ingredients]
        self.assertEqual(names, sorted(names))


    
    
    
    
        
