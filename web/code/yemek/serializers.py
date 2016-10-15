import yemek.models

from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = yemek.models.Recipe
        fields = (
            'slug',
            'title',
            'created',
            'last_updated',
            'time_prep',
            'time_cook',
            'serves',
            'note',
            'subtitle',
        )


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = yemek.models.Ingredient
        fields = (
            'id',
            'amount',
            'created',
            'last_updated',
            'name',
            'desc',
        )


class RecipeStepSerializer(serializers.ModelSerializer):

    class Meta:
        model = yemek.models.RecipeStep
        fields = (
            'id',
            'name',
            'created',
            'last_updated',
            'steporder',
        )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = yemek.models.Collection
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
        )


class RecipeSourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = yemek.models.RecipeSource
        fields = (
            'slug',
            'name',
            'created',
            'last_updated',
        )
