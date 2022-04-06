from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models import Category, Blog

NUMBER_OF_ITEMS = 50


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user('user', password='password')
        test_user.save()
        test_category = Category.objects.create(title='Test')

        for item_index in range(NUMBER_OF_ITEMS):
            Blog.objects.create(
                title=f'title {item_index}',
                content=f'description {item_index}',
                category_id=test_category.id,
            )

    def test_blog_url_exists_at_desired_location(self):
        response = self.client.get('/blog/1')
        self.assertEqual(response.status_code, 200)

    def test_blog_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'blog/home_blog_list.html')
