from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs':blogs})

def contato(request):
    return render(request, 'blog/contato.html')