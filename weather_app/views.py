import requests
from django.shortcuts import render, redirect
from .models import City, SearchHistory
from .forms import CityForm


def get_weather_data(city_name):
    api_url = f'https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['hourly']['temperature_2m'][0],
        }
    return None


def index(request):
    form = CityForm(request.POST or None)
    weather_data = None

    if request.method == 'POST' and form.is_valid():
        city_name = form.cleaned_data['name']
        city, created = City.objects.get_or_create(name=city_name)
        SearchHistory.objects.create(city=city)
        weather_data = get_weather_data(city_name)

    return render(request, 'weather_app/index.html', {'form': form, 'weather': weather_data})