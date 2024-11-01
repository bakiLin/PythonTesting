from django.shortcuts import render

recipe_list = [
        {'title': "Блинчик с мясом", 'recipe_id': 0},
        {'title': "Блинчик с творогом", 'recipe_id': 1},
        {'title': "Блинчик обыкновенный", 'recipe_id': 2}
]

def about(request):
    return render(request, 'recipe_catalog/about.html')

def index(request):
    context = {
        'recipe_list': recipe_list
    }
    return render(request, 'recipe_catalog/index.html', context)

def recipe_detail(request, pk):
    context = {
        'title': recipe_list[pk]['title'],
        'recipe_id': pk,
    }
    return render(request, 'recipe_catalog/recipe.html', context)