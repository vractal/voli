from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Recipe, Tag
# Create your views here.

# def home(request):
#
#     recipes = Recipe.objects.all()
#     tags = Tag.objects.all()
#
#
#     return render(request, 'home.html',{'recipes': recipes, 'tags':tags})



class Home(ListView):
    model = Recipe
    template_name = 'home.html'
    context_object_name = 'recipes'
    paginate_by = 14

    def get_context_data(self, **kwargs):
        # Add tags to context
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


