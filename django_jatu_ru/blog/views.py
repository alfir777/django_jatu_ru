from django.shortcuts import render

from .models import Blog


def index(request):
    blogs = Blog.objects.order_by('-created_at')
    context = {
        'blogs': blogs,
        'title': 'Мои блоги'
    }
    return render(request, template_name='blog/index.html', context=context)
