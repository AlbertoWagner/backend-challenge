import unittest
import json
from datetime import datetime

from django.test import TestCase
from rest_framework.test import APIClient

from faker import Faker
from django.urls import reverse

from products.models import Product
from products.serializers import ProductSerializer


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        fake = Faker()
        self.list_url = reverse('product-list')
        self.product_data = {
            'code': '3251490332080',
            'barcode': fake.ean13(),
            'status': 'imported',
            'imported_t': datetime.strptime("2023-07-09T00:53:57Z", "%Y-%m-%dT%H:%M:%SZ"),
            'url': fake.url(),
            'product_name': fake.name(),
            'quantity': fake.random_number(),
            'categories': fake.words(nb=3),
            'packaging': fake.words(nb=3),
            'brands': fake.company(),
            'image_url': fake.image_url(),
        }
        self.product = Product.objects.create(**self.product_data)
        self.serializer = ProductSerializer(instance=self.product)

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'Fullstack Challenge 20201026'})

    def test_list_products(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [self.serializer.data])

    def test_retrieve_product(self):
        detail_url = reverse('product-detail', args=[3251490332080])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), self.serializer.data)


if __name__ == '__main__':
    unittest.main()
