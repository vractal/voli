from django.shortcuts import render
from .models import Recipe, Tag
# Create your views here.
def home(request):
    
    recipes = Recipe.objects.all()
    return render(request, 'home.html',{'recipes': recipes})