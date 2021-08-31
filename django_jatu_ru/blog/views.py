from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Blog, Category
from .forms import BlogForm


class HomeBlog(ListView):
    model = Blog
    template_name = 'blog/home_blog_list.html'
    context_object_name = 'blog'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


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
