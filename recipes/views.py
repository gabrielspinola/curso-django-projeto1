from django.http import Http404
from django.shortcuts import render  # get_list_or_404
from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes, #[make_recipe() for _ in range(10)] #Gerador de dados randomicamente
    })

#Category
def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    
    if not recipes:
        raise Http404('Not found 😅️')
    
    #recipes = get_list_or_404(
    #    Recipe.objects.filter(
    #        category__id=category_id,
    #        is_published=True,
    #    ).order_by('-id')
    #)
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | ',
        #'title': f'{recipes[0].category.name} - Category | ' - Necessário usar essa linha apenas se o utilizar a função get_list_or_404- Ela retorna uma lista 
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()
    
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })
