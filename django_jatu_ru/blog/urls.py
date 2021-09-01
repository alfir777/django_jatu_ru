from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('test/', test, name='test'),
    # path('test/', test_send_mail, name='test'),
    path('contact/', contact, name='contact'),
    # path('', index, name='home'),
    # path('', cache_page(60)(HomeBlog.as_view()), name='home'),
    path('', HomeBlog.as_view(), name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>',
         BlogByCategory.as_view(extra_context={'title': 'Какой-то title'}),
         name='category',
         ),
    # path('blog/<int:blog_id>', view_blog, name='view_blog'),
    path('blog/<int:pk>', ViewBlog.as_view(), name='view_blog'),
    # path('blog/add-post>', add_post, name='add_post'),
    path('blog/add-post>', CreatePost.as_view(), name='add_post'),
]
