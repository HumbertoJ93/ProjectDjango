from django.shortcuts import render
from django.http import HttpRequest
from BlogApp.models import Categoria, Post
from CRUDApp.forms import PostForm

# Create your views here.

def crud(request):
    return render(request, 'crud/crud.html')



class PostFormView(HttpRequest):
    
    def index(request):
        post=PostForm()
        return render(request, "crud/post_crear.html", {"post":post})
    
    def procesar_form(request):
        post=Post()
        if  post.is_valid():
            post.save()
            post=Post()
            
        return render(request, "crud/post_crear.html", {"post":post, "mensaje": "OK"})