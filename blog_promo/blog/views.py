from django.shortcuts import render
from .models import Article

def home(request):
    return render(request, 'blog/home.html', {'articles' : Article.get_with_shape((3,3))})