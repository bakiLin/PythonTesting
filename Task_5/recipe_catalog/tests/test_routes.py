from django.test import TestCase
from django.urls import reverse
from ..models import Recipe
import unittest

class RecipeViewsTests(TestCase):
    def test_recipes_list_view(self):
        """Проверка доступности страницы списка рецептов"""
        url = reverse('recipe_catalog:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_detail(self):
        """Проверка доступности страницы деталей конкретного рецепта"""
        recipe = Recipe.objects.create(name='Test')
        url = reverse('recipe_catalog:recipe_detail', args=[recipe.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, recipe.name)

    def test_about_page_view(self):
        """Проверка доступности страницы О Нас"""
        url = reverse('recipe_catalog:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()