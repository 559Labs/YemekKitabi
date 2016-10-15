from django.conf.urls import url, include
from rest_framework import routers
import yemek.api
import yemek.views

router = routers.DefaultRouter()
router.register(r'recipe', yemek.api.RecipeViewSet)
router.register(r'ingredient', yemek.api.IngredientViewSet)
router.register(r'recipestep', yemek.api.RecipeStepViewSet)
router.register(r'collection', yemek.api.CollectionViewSet)
router.register(r'recipesource', yemek.api.RecipeSourceViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', yemek.views.HomeView.as_view(), name="yemek_home"),
)

urlpatterns += (
    # urls for Recipe
    url(r'^recipe/$', yemek.views.RecipeListView.as_view(), name='yemek_recipe_list'),
    url(r'^recipe/create/$', yemek.views.RecipeCreateView.as_view(), name='yemek_recipe_create'),
    url(r'^recipe/detail/(?P<slug>\S+)/$', yemek.views.RecipeDetailView.as_view(), name='yemek_recipe_detail'),
    url(r'^recipe/update/(?P<slug>\S+)/$', yemek.views.RecipeUpdateView.as_view(), name='yemek_recipe_update'),
)

urlpatterns += (
    # urls for Ingredient
    url(r'^ingredient/$', yemek.views.IngredientListView.as_view(), name='yemek_ingredient_list'),
    url(r'^ingredient/create/$', yemek.views.IngredientCreateView.as_view(), name='yemek_ingredient_create'),
    url(r'^ingredient/detail/(?P<id>\S+)/$', yemek.views.IngredientDetailView.as_view(), name='yemek_ingredient_detail'),
    url(r'^ingredient/update/(?P<id>\S+)/$', yemek.views.IngredientUpdateView.as_view(), name='yemek_ingredient_update'),
)

urlpatterns += (
    # urls for RecipeStep
    url(r'^recipestep/$', yemek.views.RecipeStepListView.as_view(), name='yemek_recipestep_list'),
    url(r'^recipestep/create/$', yemek.views.RecipeStepCreateView.as_view(), name='yemek_recipestep_create'),
    url(r'^recipestep/detail/(?P<id>\S+)/$', yemek.views.RecipeStepDetailView.as_view(), name='yemek_recipestep_detail'),
    url(r'^recipestep/update/(?P<id>\S+)/$', yemek.views.RecipeStepUpdateView.as_view(), name='yemek_recipestep_update'),
)

urlpatterns += (
    # urls for Collection
    url(r'^collection/$', yemek.views.CollectionListView.as_view(), name='yemek_collection_list'),
    url(r'^collection/create/$', yemek.views.CollectionCreateView.as_view(), name='yemek_collection_create'),
    url(r'^collection/detail/(?P<slug>\S+)/$', yemek.views.CollectionDetailView.as_view(), name='yemek_collection_detail'),
    url(r'^collection/update/(?P<slug>\S+)/$', yemek.views.CollectionUpdateView.as_view(), name='yemek_collection_update'),
)

urlpatterns += (
    # urls for RecipeSource
    url(r'^recipesource/$', yemek.views.RecipeSourceListView.as_view(), name='yemek_recipesource_list'),
    url(r'^recipesource/create/$', yemek.views.RecipeSourceCreateView.as_view(), name='yemek_recipesource_create'),
    url(r'^recipesource/detail/(?P<slug>\S+)/$', yemek.views.RecipeSourceDetailView.as_view(), name='yemek_recipesource_detail'),
    url(r'^recipesource/update/(?P<slug>\S+)/$', yemek.views.RecipeSourceUpdateView.as_view(), name='yemek_recipesource_update'),
)
