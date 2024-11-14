from django.shortcuts import render
from .models import Recipe

def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    recipe_list = Recipe.objects.all()
    context = {
        'recipe_list': recipe_list
    }
    return render(request, 'recipe_catalog/index.html', context)

def recipe_detail(request, pk):
    template_name = 'recipe_catalog/recipe.html'
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'title': recipe.name,
        'recipe_id': pk,
        'recipe_desc': recipe.desc,
        'ingredients': recipe.recipeingredient_set.all().order_by('ingredient__name')
    }
    return render(request, template_name, context)
