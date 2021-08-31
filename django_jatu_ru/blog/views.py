from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Blog, Category
from .forms import BlogForm
from .utils import MyMixin


class HomeBlog(MyMixin, ListView):
    model = Blog
    template_name = 'blog/home_blog_list.html'
    context_object_name = 'blog'
    mixin_prop = 'Hello World'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('category')


class BlogByCategory(ListView):
    model = Blog
    template_name = 'blog/home_blog_list.html'
    context_object_name = 'blog'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewBlog(DetailView):
    model = Blog
    context_object_name = 'blog_item'
    # pk_url_kwarg = 'blog_id'
    # template_name = 'blog/blog_detail.html'


class CreatePost(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blog/add_post.html'
    # success_url = reverse_lazy('home')
    login_url = '/admin/'
    # raise_exception = True


# def index(request):
#     blogs = Blog.objects.all()
#     context = {
#         'blogs': blogs,
#         'title': 'Мои блоги',
#     }
#     return render(request, template_name='blog/index.html', context=context)


# def get_category(request, category_id):
#     blogs = Blog.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'blog/category.html', {'blogs': blogs, 'category': category})


# def view_blog(request, blog_id):
#     # blog_item = Blog.objects.get(pk=blog_id)
#     blog_item = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog/view_blog.html', {'blog_item': blog_item})


# def add_post(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             post = form.save()
#             return redirect(post)
#     else:
#         form = BlogForm()
#     return render(request, 'blog/add_post.html', {'form': form})
