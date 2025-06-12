
import requests

city_name="New Delhi"
API_KEY="724d7985285d1ba228e6839d7d096121"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"


response= requests.get(url)
if response.status_code==200:
  data=response.json()
  print('location is',data['name'])
  print('weather is',data['weather'][0]['description'])
  print('current temperature is',data['main']['temp'])
  print('current temperature feels_like',data['main']['feels_like'])
  print('current humidity feels_like',data['main']['humidity'])

city_name="Andhra Pradesh"
API_KEY="724d7985285d1ba228e6839d7d096121"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"


response= requests.get(url)
if response.status_code==200:
  data=response.json()
  print('location is',data['name'])
  print('weather is',data['weather'][0]['description'])
  print('current temperature is',data['main']['temp'])
  print('current temperature feels_like',data['main']['feels_like'])
  print('current humidity feels_like',data['main']['humidity'])


  