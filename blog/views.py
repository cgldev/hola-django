from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.
from .models import Post
from .forms import PostForm

# vista listar
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

#vista detalle
class PostDetailView(DetailView):
    model = Post

#vista eliminar
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

#vista actualizar
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  
    success_url = reverse_lazy('blog:post_list')

#vista crear
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm    
    success_url = reverse_lazy('blog:post_list')    