import os
import django
from django.test import TestCase
from django.urls import reverse

os.environ['DJANGO_SETTINGS_MODULE'] = 'weather_project.settings'
django.setup()

from .models import City, SearchHistory

# Ваши тесты здесь
class WeatherAppTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Weather Forecast")

    def test_search_city(self):
        response = self.client.post(reverse('index'), {'name': 'London'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Weather in London')
        self.assertTrue(City.objects.filter(name='London').exists())
        self.assertTrue(SearchHistory.objects.filter(city__name='London').exists())