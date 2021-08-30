from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('blog/<int:blog_id>', view_blog, name='view_blog'),
    path('blog/add-post>', add_post, name='add_post'),

]
