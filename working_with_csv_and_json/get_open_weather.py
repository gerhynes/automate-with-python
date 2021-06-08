#! python3
# get_open_weather.py - Prints the weather for a location from the command line

import os, json, requests, sys
from dotenv import load_dotenv
load_dotenv()

APPID = os.environ['APPID']

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: get_open_weather.py city_name, 2-letter_country_code')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}s&cnt=3&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()
# Uncomment to see the raw JSON
# print(response.text)

# Load JSON data into a Python variable
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])