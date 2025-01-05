from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import views
from django.core.exceptions import PermissionDenied

from .models import Recipe, Ingredient, RecipeIngredient
from .forms import UserForm, IngredientForm, RecipeForm, RecipeIngredientForm

def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    recipe_list = Recipe.objects.all()
    template = 'recipe_catalog/index.html'
    context = {
        'recipe_list': recipe_list
    }

    return render(request, template, context)

def recipe_detail(request, pk):
    template = 'recipe_catalog/recipe.html'
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.recipeingredient_set.all().order_by('ingredient__name')
    total_weight = calc_weight(ingredients)

    context = {
        'title': recipe.name,
        'recipe_id': pk,
        'recipe_desc': recipe.desc,
        'ingredients': recipe.recipeingredient_set.all().order_by('ingredient__name'),
        'total_weight': total_weight,
        'author': recipe.author,
    }

    return render(request, template, context)

def calc_weight(ingredients):
    total = 0
    for ingredient in ingredients:
        total += ingredient.weight
    return total

def form_user_test(request):
    """Тестовая форма для пользователя."""
    template = 'recipe_catalog/user_form_test.html'
    if request.GET:
        form = UserForm(request.GET)
        if form.is_valid():
            pass
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, template, context)

def ingredient(request):
    """Форма для ингредиентов."""
    if not request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/auth/login/")
    
    template = 'recipe_catalog/ingredient_form.html'
    form = IngredientForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, template, context)

def ingredient_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/auth/login/")
    """Форма для редактирования ингредиентов."""
    template = 'recipe_catalog/ingredient_edit.html'
    instance = get_object_or_404(Ingredient, pk=pk)
    form = IngredientForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template, context)

def ingredient_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/auth/login/")
    """Форма для удаления ингредиента."""
    instance = get_object_or_404(Ingredient, pk=pk)
    instance.delete()
    return redirect("http://127.0.0.1:8000/all_ingredients/")

def recipe(request):
    if not request.user.is_authenticated:
        return redirect("http://127.0.0.1:8000/auth/login/")

    template = 'recipe_catalog/recipe_form.html'
    form = RecipeForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
    context = {'form': form}
    return render(request, template, context)

def recipe_edit(request, pk):
    try:
        instance = Recipe.objects.get(id=pk, author=request.user)
    except Recipe.DoesNotExist:
        raise Http404("Вы не автор рецепта.")

    template = 'recipe_catalog/recipe_form.html'
    # instance = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, template, context)

def recipe_delete(request, pk):
    """Форма для удаления рецепта."""
    try:
        instance = Recipe.objects.get(id=pk, author=request.user)
    except Recipe.DoesNotExist:
        raise Http404("Вы не автор рецепта.")
    
    instance = get_object_or_404(Recipe, pk=pk)
    instance.delete()
    return redirect("http://127.0.0.1:8000/")
    
    
def all_ingredients(request):
    ingredients_list = Ingredient.objects.all()
    template = 'recipe_catalog/all_ingredients.html'
    context = {
        'ingredients_list': ingredients_list
    }
    return render(request, template, context)

def ingredient_to_recipe(request, pk):
    not request.user.is_authenticated
    try:
        instance = Recipe.objects.get(id=pk, author=request.user)
    except Recipe.DoesNotExist:
        raise Http404("Вы не автор рецепта.")

    recipe = Recipe.objects.get(id=pk)
    form = RecipeIngredientForm(request.POST or None)
    template = 'recipe_catalog/ingredient_to_recipe.html'
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance.recipe = recipe
        instance.save()
    context = {'form': form}
    return render(request, template, context)

def delete_recipe_ingredient(request, pk, ingredient_id):
    try:
        instance = Recipe.objects.get(id=pk, author=request.user)
    except Recipe.DoesNotExist:
        raise Http404("Вы не автор рецепта.")

    template = 'http://127.0.0.1:8000/recipe/' + str(pk)
    ingredient = RecipeIngredient.objects.get(id=ingredient_id, recipe__id=pk)
    ingredient.delete()
    return redirect(template)