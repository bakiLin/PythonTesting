from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Recipe, Ingredient, RecipeIngredient

class RecipeLogicTests(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='author', password='password123')
        self.other_user = User.objects.create_user(username='other_user', password='password123')

        self.ingredient = Ingredient.objects.create(name='Сахар')

        self.recipe = Recipe.objects.create(name='Пирог', author=self.author)
        self.recipe_ingredient = RecipeIngredient.objects.create(
            recipe=self.recipe, ingredient=self.ingredient, weight=100
        )

    # Тесты для создания рецептов
    def test_create_recipe_requires_authentication(self):
        """Создание рецепта неавторизованным"""
        response = self.client.post(reverse('recipe_catalog:add_recipe'), {'name': 'Торт'})
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('recipe_catalog:login'), response.url)

    def test_create_recipe_authorized(self):
        """"Создание рецепта авторизованным"""
        self.client.login(username='author', password='password123')
        response = self.client.post(reverse('recipe_catalog:add_recipe'), {'name': 'Торт'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_edit_recipe_authorized(self):
        """Редактирование рецепта авторизованным"""
        self.client.login(username='author', password='password123')
        response = self.client.post(
            reverse('recipe_catalog:recipe_edit', kwargs={'pk': self.recipe.id}),
            {'name': 'Обновленный Пирог'}
        )
        self.assertEqual(response.status_code, 200)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.name, 'Пирог')

    def test_edit_recipe_other_user(self):
        """Редактирование чужого рецепта"""
        self.client.login(username='other_user', password='password123')
        response = self.client.post(
            reverse('recipe_catalog:recipe_edit', kwargs={'pk': self.recipe.id}),
            {'name': 'Обновленный Пирог'}
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_recipe_authorized(self):
        """Удаление рецепта авторизованным"""
        self.client.login(username='author', password='password123')
        response = self.client.post(reverse('recipe_catalog:recipe_delete', kwargs={'pk': self.recipe.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_delete_recipe_other_user(self):
        """Удаление чужого рецепта"""
        self.client.login(username='other_user', password='password123')
        response = self.client.post(reverse('recipe_catalog:recipe_delete', kwargs={'pk': self.recipe.id}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_add_ingredient_authorized(self):
        """Добавление ингредиента авторизованным"""
        self.client.login(username='author', password='password123')
        response = self.client.post(reverse('recipe_catalog:add_ingredient'), {
            'name': 'Мука',
            'weight': '300'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ingredient.objects.count(), 2)

    def test_edit_recipe_ingredient(self):
        """Редактирование ингредиента рецепта"""
        self.client.login(username='author', password='password123')
        response = self.client.post(
            reverse('recipe_catalog:ingredient_edit', kwargs={'pk': self.recipe.id}),
            {'weight': 150}
        )
        self.assertEqual(response.status_code, 200)
        self.recipe_ingredient.refresh_from_db()
        self.assertEqual(self.recipe_ingredient.weight, 100)

    def test_edit_recipe_ingredient_other_user(self):
        """Редактирование ингредиента чужого рецепта"""
        self.client.login(username='other_user', password='password123')
        response = self.client.post(
            reverse('recipe_catalog:ingredient_to_recipe', kwargs={'pk': self.recipe.id}),
            {'weight': 150}
        )
        self.assertEqual(response.status_code, 404)
        self.recipe_ingredient.refresh_from_db()

    def test_delete_recipe_ingredient(self):
        """Удаление ингредиента рецепта"""
        self.client.login(username='author', password='password123')
        response = self.client.post(reverse('recipe_catalog:delete_recipe_ingredient', kwargs={'pk': self.recipe.id, 'ingredient_id': self.recipe_ingredient.id}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(RecipeIngredient.objects.count(), 0)

    def test_delete_recipe_ingredient_other_user(self):
        """Удаление ингредиента чужого рецепта"""
        self.client.login(username='other_user', password='password123')
        response = self.client.post(reverse('recipe_catalog:delete_recipe_ingredient', kwargs={'pk': self.recipe.id, 'ingredient_id': self.recipe_ingredient.id}))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(RecipeIngredient.objects.count(), 1)