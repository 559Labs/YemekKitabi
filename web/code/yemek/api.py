import yemek.models
import yemek.serializers
from rest_framework import viewsets, permissions


class RecipeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Recipe class"""
    queryset = yemek.models.Recipe.objects.all()
    serializer_class = yemek.serializers.RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ingredient class"""
    queryset = yemek.models.Ingredient.objects.all()
    serializer_class = yemek.serializers.IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecipeStepViewSet(viewsets.ModelViewSet):
    """ViewSet for the RecipeStep class"""
    queryset = yemek.models.RecipeStep.objects.all()
    serializer_class = yemek.serializers.RecipeStepSerializer
    permission_classes = [permissions.IsAuthenticated]

class CollectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Collection class"""
    queryset = yemek.models.Collection.objects.all()
    serializer_class = yemek.serializers.CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecipeSourceViewSet(viewsets.ModelViewSet):
    """ViewSet for the RecipeSource class"""
    queryset = yemek.models.RecipeSource.objects.all()
    serializer_class = yemek.serializers.RecipeSourceSerializer
    permission_classes = [permissions.IsAuthenticated]
