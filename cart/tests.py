from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status


class CartTest(APITestCase):

    URL_BASE = "http://localhost:7000/api/"

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_return_200_get_cart(self):
        response = self.client.get(self.URL_BASE + "carts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)