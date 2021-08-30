from django.urls import path

from .views import index, get_category, view_blog

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('blog/<int:blog_id>', view_blog, name='view_blog'),
]
