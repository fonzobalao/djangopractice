from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
        #query from database
    }
    return render(request, 'practice/home.html', context)

def about(request):
    return render(request, 'practice/about.html', {'title': 'About'})


# RegistrationModelForm

