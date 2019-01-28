import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.
def index(request):
         
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=916d52446e63a22fe80060280abc21e1'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()


    city_data=[]

    
    
    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather={
            'city': city.name,
            'temp': r['main']['temp'],
            'desc': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        
        city_data.append(city_weather)

    context ={'city_data': city_data, 'form': form}

    return render(request, 'weather/index.html', context)