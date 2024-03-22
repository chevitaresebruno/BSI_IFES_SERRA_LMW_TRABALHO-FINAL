from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def aula_um(request):
    return render(request, 'blog/aula_um.html', {})

def aula_dois(request):
    return render(request, 'blog/aula_dois.html', {})
