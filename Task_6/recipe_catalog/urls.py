from django.urls import path
from django.contrib.auth import views
from .views import (about, index, recipe_detail, form_user_test, 
                    ingredient, ingredient_edit, ingredient_delete, 
                    all_ingredients, recipe, ingredient_to_recipe, 
                    delete_recipe_ingredient, recipe_edit, recipe_delete)

app_name = 'recipe_catalog'

urlpatterns = [
    path('', index, name='home'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('about/', about, name='about'),
    path('user_form_test/', form_user_test, name='create_user_test'),
    path('add_ingredient/', ingredient, name='add_ingredient'),
    path('ingredient/<int:pk>/edit/', ingredient_edit, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete/', ingredient_delete, name='ingredient_delete'),
    path('all_ingredients/', all_ingredients, name='all_ingredients'),
    path('add_recipe/', recipe, name='add_recipe'),
    path('recipe/<int:pk>/add/', ingredient_to_recipe, name='ingredient_to_recipe'),
    path('recipe/<int:pk>/delete/<int:ingredient_id>/', delete_recipe_ingredient, name='delete_recipe_ingredient'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    path('auth/login/', views.LoginView.as_view(template_name='recipe_catalog/login.html'), name='login'), 
    path('auth/logout/', views.LogoutView.as_view(), name='logout'), 
]