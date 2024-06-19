from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class WatchListAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.watch_list_url = reverse('watch_list')

    def test_get_watch_list(self):
        response = self.client.get(self.watch_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
