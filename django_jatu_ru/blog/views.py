from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog, Category
from .forms import BlogForm


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


def view_blog(request, blog_id):
    # blog_item = Blog.objects.get(pk=blog_id)
    blog_item = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/view_blog.html', {'blog_item': blog_item})


def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            post = form.save()
            return redirect(post)
    else:
        form = BlogForm()
    return render(request, 'blog/add_post.html', {'form': form})
