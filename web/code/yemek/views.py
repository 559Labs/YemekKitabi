from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Recipe, Ingredient, RecipeStep, Collection, RecipeSource
from .forms import RecipeForm, IngredientForm, RecipeStepForm, CollectionForm, RecipeSourceForm

class HomeView(TemplateView):
    template_name = "yemek/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context

class RecipeListView(ListView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm

class IngredientListView(ListView):
    model = Ingredient

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm

class IngredientDetailView(DetailView):
    model = Ingredient

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm

class RecipeStepListView(ListView):
    model = RecipeStep

class RecipeStepCreateView(CreateView):
    model = RecipeStep
    form_class = RecipeStepForm

class RecipeStepDetailView(DetailView):
    model = RecipeStep

class RecipeStepUpdateView(UpdateView):
    model = RecipeStep
    form_class = RecipeStepForm

class CollectionListView(ListView):
    model = Collection

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm

class CollectionDetailView(DetailView):
    model = Collection

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm

class RecipeSourceListView(ListView):
    model = RecipeSource

class RecipeSourceCreateView(CreateView):
    model = RecipeSource
    form_class = RecipeSourceForm

class RecipeSourceDetailView(DetailView):
    model = RecipeSource

class RecipeSourceUpdateView(UpdateView):
    model = RecipeSource
    form_class = RecipeSourceForm
