from django.shortcuts import render

# Create your views here.
# Main app views
def index(request):
    return render(request, 'Main/index.html')