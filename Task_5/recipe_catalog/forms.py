from django import forms
from .models import Ingredient, Recipe, RecipeIngredient

class UserForm(forms.Form):
    """Тестовая форма к теории."""
    first_name = forms.CharField(label='Имя',max_length=20)
    last_name = forms.CharField(label='Фамилия', required=False)
    user_email = forms.EmailField(label='Email', required=False)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name',)
        labels = {
            'name': 'Название'
        }
        

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'desc',)
        labels = {
            'name': 'Название',
            'desc': 'Описание',
        }
        exclude = ('author',)

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'weight',)

    def clean(self):
        cleaned_data = super().clean()
        weight = cleaned_data.get('weight')
        
        if weight <= 0:
            raise forms.ValidationError("Вес и количество должны быть положительными числами.")
        
        return cleaned_data

