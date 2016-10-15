import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Recipe, Ingredient, RecipeStep, Collection, RecipeSource
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_recipe(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["time_prep"] = "time_prep"
    defaults["time_cook"] = "time_cook"
    defaults["serves"] = "serves"
    defaults["note"] = "note"
    defaults["subtitle"] = "subtitle"
    defaults.update(**kwargs)
    if "collection" not in defaults:
        defaults["collection"] = create_collection()
    if "source" not in defaults:
        defaults["source"] = create_recipesource()
    return Recipe.objects.create(**defaults)


def create_ingredient(**kwargs):
    defaults = {}
    defaults["amount"] = "amount"
    defaults["name"] = "name"
    defaults["desc"] = "desc"
    defaults.update(**kwargs)
    if "Recipe" not in defaults:
        defaults["Recipe"] = create_recipe()
    return Ingredient.objects.create(**defaults)


def create_recipestep(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["steporder"] = "steporder"
    defaults.update(**kwargs)
    return RecipeStep.objects.create(**defaults)


def create_collection(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Collection.objects.create(**defaults)


def create_recipesource(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return RecipeSource.objects.create(**defaults)


class RecipeViewTest(unittest.TestCase):
    '''
    Tests for Recipe
    '''
    def setUp(self):
        self.client = Client()

    def test_list_recipe(self):
        url = reverse('yemek_recipe_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_recipe(self):
        url = reverse('yemek_recipe_create')
        data = {
            "title": "title",
            "time_prep": "time_prep",
            "time_cook": "time_cook",
            "serves": "serves",
            "note": "note",
            "subtitle": "subtitle",
            "collection": create_collection().id,
            "source": create_recipesource().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_recipe(self):
        recipe = create_recipe()
        url = reverse('yemek_recipe_detail', args=[recipe.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_recipe(self):
        recipe = create_recipe()
        data = {
            "title": "title",
            "time_prep": "time_prep",
            "time_cook": "time_cook",
            "serves": "serves",
            "note": "note",
            "subtitle": "subtitle",
            "collection": create_collection().id,
            "source": create_recipesource().id,
        }
        url = reverse('yemek_recipe_update', args=[recipe.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IngredientViewTest(unittest.TestCase):
    '''
    Tests for Ingredient
    '''
    def setUp(self):
        self.client = Client()

    def test_list_ingredient(self):
        url = reverse('yemek_ingredient_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_ingredient(self):
        url = reverse('yemek_ingredient_create')
        data = {
            "amount": "amount",
            "name": "name",
            "desc": "desc",
            "Recipe": create_recipe().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_ingredient(self):
        ingredient = create_ingredient()
        url = reverse('yemek_ingredient_detail', args=[ingredient.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_ingredient(self):
        ingredient = create_ingredient()
        data = {
            "amount": "amount",
            "name": "name",
            "desc": "desc",
            "Recipe": create_recipe().id,
        }
        url = reverse('yemek_ingredient_update', args=[ingredient.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RecipeStepViewTest(unittest.TestCase):
    '''
    Tests for RecipeStep
    '''
    def setUp(self):
        self.client = Client()

    def test_list_recipestep(self):
        url = reverse('yemek_recipestep_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_recipestep(self):
        url = reverse('yemek_recipestep_create')
        data = {
            "name": "name",
            "steporder": "steporder",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_recipestep(self):
        recipestep = create_recipestep()
        url = reverse('yemek_recipestep_detail', args=[recipestep.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_recipestep(self):
        recipestep = create_recipestep()
        data = {
            "name": "name",
            "steporder": "steporder",
        }
        url = reverse('yemek_recipestep_update', args=[recipestep.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CollectionViewTest(unittest.TestCase):
    '''
    Tests for Collection
    '''
    def setUp(self):
        self.client = Client()

    def test_list_collection(self):
        url = reverse('yemek_collection_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_collection(self):
        url = reverse('yemek_collection_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_collection(self):
        collection = create_collection()
        url = reverse('yemek_collection_detail', args=[collection.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_collection(self):
        collection = create_collection()
        data = {
            "name": "name",
        }
        url = reverse('yemek_collection_update', args=[collection.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RecipeSourceViewTest(unittest.TestCase):
    '''
    Tests for RecipeSource
    '''
    def setUp(self):
        self.client = Client()

    def test_list_recipesource(self):
        url = reverse('yemek_recipesource_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_recipesource(self):
        url = reverse('yemek_recipesource_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_recipesource(self):
        recipesource = create_recipesource()
        url = reverse('yemek_recipesource_detail', args=[recipesource.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_recipesource(self):
        recipesource = create_recipesource()
        data = {
            "name": "name",
        }
        url = reverse('yemek_recipesource_update', args=[recipesource.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


