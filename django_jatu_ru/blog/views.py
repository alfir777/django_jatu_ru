from django.shortcuts import render

from .models import Blog


def index(request):
    blogs = Blog.objects.all
    context = {
        'blogs': blogs,
        'title': 'Мои блоги'
    }
    return render(request, template_name='blog/index.html', context=context)
