from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home_site/home.html')


def about(request):
    return render(request, 'home_site/about.html')