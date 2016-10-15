from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

class Recipe(models.Model):
    # Fields
    title = models.CharField(max_length=255, default="", blank=True)
    subtitle = models.CharField(max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    time_prep = models.CharField(max_length=64, default="", blank=True)
    time_cook = models.CharField(max_length=64, default="", blank=True)
    serves = models.CharField(max_length=30, default="", blank=True)
    note = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    collection = models.ForeignKey('yemek.Collection', )
    source = models.ForeignKey('yemek.RecipeSource', )
    class Meta:
        ordering = ('title','subtitle',)
    def __str__(self):
        return u'%s' % self.title

    def get_ingredients(self):
        return Ingredient.objects.filter(recipe=self)
    def get_steps(self):
        return RecipeStep.objects.filter(recipe=self)

    def get_ingredient_count(self):
        return Ingredient.objects.filter(recipe=self).count()
    def get_step_count(self):
        return RecipeStep.objects.filter(recipe=self).count()

    def get_absolute_url(self):
        return reverse('yemek_recipe_detail', args=(self.slug,))
    def get_update_url(self):
        return reverse('yemek_recipe_update', args=(self.slug,))

class Ingredient(models.Model):
    # Fields
    amount = models.CharField(max_length=255, default="", blank=True)
    name = models.CharField(max_length=255, default="", blank=True)
    desc = models.CharField(max_length=255, default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    recipe = models.ForeignKey(Recipe, blank=True, null=True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('yemek_ingredient_detail', args=(self.id,))
    def get_update_url(self):
        return reverse('yemek_ingredient_update', args=(self.id,))

class RecipeStep(models.Model):
    # Fields
    steporder = models.IntegerField(default=0)
    name = models.TextField(default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    recipe = models.ForeignKey(Recipe, blank=True, null=True)
    class Meta:
        ordering = ('steporder','name',)
    def __str__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('yemek_recipestep_detail', args=(self.id,))
    def get_update_url(self):
        return reverse('yemek_recipestep_update', args=(self.id,))

class Collection(models.Model):
    # Fields
    name = models.CharField(max_length=255, default="", blank=True)
    order = models.IntegerField(default=999)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        ordering = ('order','name',)
    def __str__(self):
        return u'%s' % self.name

    def get_recipes(self):
        return Recipe.objects.filter(collection=self)
    get_recipes.short_description = "Recipes"
    def get_num_recipes(self):
        return Recipe.objects.filter(collection=self).count()
    get_num_recipes.short_description = "Recipe Count"

    def get_absolute_url(self):
        return reverse('yemek_collection_detail', args=(self.slug,))
    def get_update_url(self):
        return reverse('yemek_collection_update', args=(self.slug,))

class RecipeSource(models.Model):
    # Fields
    name = models.CharField(max_length=255, default="", blank=True)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return u'%s' % self.name

    def get_recipes(self):
        return Recipe.objects.filter(source=self)
    get_recipes.short_description = "Recipes"

    def get_num_recipes(self):
        return Recipe.objects.filter(source=self).count()
    get_num_recipes.short_description = "Recipe Count"


    get_num_recipes.short_description = "Recipe Count"
    def get_absolute_url(self):
        return reverse('yemek_recipesource_detail', args=(self.slug,))
    def get_update_url(self):
        return reverse('yemek_recipesource_update', args=(self.slug,))
