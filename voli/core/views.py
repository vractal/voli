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
        filter = self.request.POST.getlist("tag")
        clear = self.request.POST.get("clear")


        if filter and not clear:
            tags = [Tag.objects.get(name=tag) for tag in filter]
            sets = [set(tag.recipes.all()) for tag in tags]
            recipes_set = set.intersection(*sets)
            self.object_list = list(recipes_set)
            self.request.session['session_filter'] = filter
        else:
            self.object_list = Recipe.objects.all()
            self.request.session['session_filter'] = None


        context = self.get_context_data(**kwargs)

        return render(request, 'home.html', context)



    def get_context_data(self, **kwargs):
        # Add tags to context
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()

        return context

    def get_queryset(self):
        try:
            filter = self.request.session['session_filter']
            tags = [Tag.objects.get(name=tag) for tag in filter]
            sets = [set(tag.recipes.all()) for tag in tags]
            recipes_set = set.intersection(*sets)
            queryset = list(recipes_set)
        except:
            queryset = super().get_queryset()

        return queryset