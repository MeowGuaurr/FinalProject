from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

#dictionary for news posts
posts = [
    { 
        'author': 'Reyna',
        'title': 'Test1',
        'content': 'Test content',
        'date_posted': 'today'
    },
    { 
        'author': 'Mercedes',
        'title': 'Test2',
        'content': 'Test content2',
        'date_posted': 'tomorrow'
    }
]
