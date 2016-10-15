from django.contrib import admin
from django import forms
from .models import Recipe, Ingredient, RecipeStep, Collection, RecipeSource
from django.core.urlresolvers import reverse

"""
Inlines
"""
class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 20
    suit_classes = 'suit-tab suit-tab-ingredients'

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 20
    suit_classes = 'suit-tab suit-tab-steps'

class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 0
    suit_classes = 'suit-tab suit-tab-recipes'
    fields = ['title','subtitle','collection',]

"""
Recipe Admin
"""
class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm
    list_display = ['title', 'subtitle', ]
    readonly_fields = ['created', 'last_updated']
    inlines = [IngredientInline, RecipeStepInline,]
    fieldsets = [
        (None, {
            'classes': ('suit-tab','suit-tab-detail'),
            'fields': [
                'title','subtitle',
                'collection','source',
                'time_prep','time_cook','serves',
                'note',
            ],
        }),
    ]
    suit_form_tabs = (
        ('detail','Basic Info'),
        ('ingredients','Ingredients'),
        ('steps','Steps'),
    )
admin.site.register(Recipe, RecipeAdmin)

"""
Ingredient Admin
"""
class IngredientAdminForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
class IngredientAdmin(admin.ModelAdmin):
    form = IngredientAdminForm
    list_display = ['amount', 'name', 'desc', 'recipe',
                    'created', 'last_updated', ]
    readonly_fields = ['created', 'last_updated']
admin.site.register(Ingredient, IngredientAdmin)

"""
Recipe Step Admin
"""
class RecipeStepAdminForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = '__all__'
class RecipeStepAdmin(admin.ModelAdmin):
    form = RecipeStepAdminForm
    list_display = ['recipe', 'steporder', 'name',
                    'created', 'last_updated', ]
    readonly_fields = ['created', 'last_updated']
admin.site.register(RecipeStep, RecipeStepAdmin)

"""
Collection Admin
"""
class CollectionAdminForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'
class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm
    list_display = ['name', 'order', 'get_num_recipes',
                    'created', 'last_updated']
    readonly_fields = ['created', 'last_updated']
admin.site.register(Collection, CollectionAdmin)

"""
RecipeSource Admin
"""
class RecipeSourceAdminForm(forms.ModelForm):
    class Meta:
        model = RecipeSource
        fields = '__all__'
class RecipeSourceAdmin(admin.ModelAdmin):
    form = RecipeSourceAdminForm
    list_display = ['name', 'get_num_recipes',
                    'created', 'last_updated']
    readonly_fields = ['created', 'last_updated']
    inlines = [RecipeInline,]
    fieldsets = [
        (None, {
            'classes': ('suit-tab','suit-tab-detail'),
            'fields': [
                'name',
            ],
        }),
    ]
    suit_form_tabs = (
        ('detail','Basic Info'),
        ('recipes','Recipes'),
    )
admin.site.register(RecipeSource, RecipeSourceAdmin)
