from django.shortcuts import render

# Create your views here.
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': post_list})
