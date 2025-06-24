from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje":"Hola desde python"}
    return render(request, 'myapp/index.html', context)