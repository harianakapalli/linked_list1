from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    #city="visakhapatnam"
    city = request.GET.get("city")
    apikey ="375ed40dcdaa61ab88536f86b0cf1f30"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    response = requests.get(url)
    resp =response.json()
    paylode = {
        "city" : resp['name'],
        "weather": resp['weather'][0]['main'],
        "kelvin":(int(resp['main']['temp'])),
        'celcius':(int(resp['main']['temp']))-273,
        'weatherIcon' : resp['weather'][0]['icon']
    }
    context ={"resp":paylode}
    return render(request,"index.html",context)