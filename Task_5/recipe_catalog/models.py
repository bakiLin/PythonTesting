from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

User = get_user_model()

class Ingredient(models.Model):
    """Составная часть рецепта."""
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    """Вкусное делается по рецепту."""
    name = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    desc = models.CharField(max_length=300, default="")
    author = models.ForeignKey(User, verbose_name='Автор рецепта', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    """Один ингредиент может быть
    в нескольких рецептах,
    как и в одном рецепте может быть
    несколько ингредиентов."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name}'
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique recipes ingredients'
            )
        ]