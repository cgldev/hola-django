from django.shortcuts import render, redirect

# Create your views here.
from .models import Post
from .forms import PostForm

def post_list(request):
    busqueda=request.GET.get('busqueda', None)
    if busqueda:
        post_list = Post.objects.filter(titulo__icontains=busqueda)
    else:
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': post_list})

#vista del formulario

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', context={'form': form})