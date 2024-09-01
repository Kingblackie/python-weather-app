from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import string

load_dotenv()

def get_current_weather(city):
  request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
  weather_data = requests.get(request_url).json()
  return weather_data

if __name__ == '__main__':
  print('\n*** Get Weather Conditions ***\n')
  city = input('Please enter a city: ')
  
  # Check for empty strings or strings with only spaces
  if not bool(city.strip()):
    city = 'Lagos'
    
  weather_data = get_current_weather(city)
  print('\n') 
  pprint(weather_data)

