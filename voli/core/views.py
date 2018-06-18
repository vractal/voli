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

    # filtro por tag. Recebe um nome, adiciona no contexto da sessao, mostra o formulario de acordo (tags com checkbox) e o
    # query também
# Quero pegar uma tag por post request e retornar a pagina selecionando só os que tem a tag
    def post(self, request,*args,**kwargs):
        # Porque o dicionario do 'tag` retorna apenas o ultimo valor? o responsavel eh o MULTIVALUEDICT. Query dict
        # na documentacao ele explicita isso. PORque retornar apenas o ultimo valor??
        filter = self.request.POST.getlist("tag","")
        # Escrever sobre como achei que tinha que escrever essa linha de baixo
        if filter:
            tag = Tag.objects.get(name=filter[0])
            recipes = [recipe for recipe in tag.recipes.all()]
            if len(filter) > 0:
                for t in filter:
                    tag = Tag.objects.get(name=t)
                    r2 = [recipe for recipe in tag.recipes.all()]
                    recipes = list(set(recipes).intersection(r2))
            self.object_list = recipes
        else:
            self.object_list = Recipe.objects.all()
        context = self.get_context_data(**kwargs)
        context['session_filter'] = filter
        return render(request, 'home.html', context)



    def get_context_data(self, **kwargs):
        # Add tags to context
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
