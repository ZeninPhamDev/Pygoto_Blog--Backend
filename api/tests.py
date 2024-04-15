from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Post, Category


# Create your tests here.
class PostTests(APITestCase):
    def test_view_posts(self):
        url = reverse('api:list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='Python')

        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        data = {
            'title': 'new', 'author':1,
            'excerpt': 'new', 'content': 'new'
        }
        url = reverse('api:list_create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
