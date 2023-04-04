from django.shortcuts import render
from BlogApp.models import Categoria, Post

# Create your views here.

def crud(request):
    return render(request, 'crud/crud.html')


#------- CRUD READ -------- 
def leer_post(request):
    posts=Post.objects.all()
    return render(request, "crud/leer_post.html", {"posts":posts})