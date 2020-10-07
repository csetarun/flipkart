from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from rest_framework.test import APITestCase

from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from dashboard import views

class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_product_list(self):
        request = self.factory.get('/product/')
        response = views.ProductList.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
    
    def test_review_list(self):
        request = self.factory.get('/review/')
        response = views.ReviewList.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
    