from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Item

class CategoryTests(APITestCase):
    def test_create_category(self):
        url = reverse('category-list-create')
        data = {'name': 'Health Institutions'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Health Institutions')

class ItemTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Health Institutions')

    def test_create_item(self):
        url = reverse('item-list-create')
        data = {'category': self.category.id, 'name': 'Hospital', 'unique_attributes': {'Location': 'City Center'}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Hospital')

    def test_search_item(self):
        Item.objects.create(category=self.category, name='Hospital', unique_attributes={'Location': 'City Center'})
        url = reverse('item-list-create')
        response = self.client.get(url, {'search': 'Hospital'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
