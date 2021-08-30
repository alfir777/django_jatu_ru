from django.shortcuts import render

from .models import Blog, Category


def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'title': 'Мои блоги',
    }
    return render(request, template_name='blog/index.html', context=context)


def get_category(request, category_id):
    blogs = Blog.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html', {'blogs': blogs, 'category': category})
