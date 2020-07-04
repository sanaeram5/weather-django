from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    res=requests.get('https://ipinfo.io/')
    data=res.json()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8214e2e9f93222b771d3b04d18ee00ce"
    city= data['city']
    r=requests.get(url.format(city)).json()
    context={
        'city':city,'temperature':r['main']['temp'],'description':r['weather'][0]['description'],
    }
    return render(request, 'weather/weather.html',context)
