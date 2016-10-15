from django import forms
from .models import Recipe, Ingredient, RecipeStep, Collection, RecipeSource


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'subtitle',
                  'time_prep', 'time_cook', 'serves', 'note',
                  'collection', 'source', ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['amount', 'name', 'desc', 'recipe']

class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ['name', 'steporder', 'recipe']


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = ['name']


class RecipeSourceForm(forms.ModelForm):
    class Meta:
        model = RecipeSource
        fields = ['name']
