from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blogs.html')

def contato(request):
    return render(request, 'blog/contato.html')