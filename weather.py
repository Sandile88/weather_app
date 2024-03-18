import requests
import json
import os
import pycountry
from dotenv import load_dotenv
from dataclasses import dataclass
from icon_symbols import *


load_dotenv()
api_key = os.environ['API_KEY']    

@dataclass
class WeatherData:

    main: str
    description: str
    icon: str
    temperature: float
    speed: float

    def __str__(self) -> str:
        output = '\n'.join([f" {key}: {value}°C" if 'temp' or 'feel_like'  in key  else f"   {key}: {value}" for key, value in self.temperature.items() if key in ['temp', 'feels_like', 'temp_min', 'temp_max']])
        symbol = icon_symbols.get(self.icon, self.icon)
        return f"\nCurrent weather:\n\nMain: {self.main}, {self.description}\n Icon: {symbol}\nTemperatures: \n{output}\nPressure: {self.temperature['pressure']}hPa\nHumidity: {self.temperature['humidity']}% \nSpeed: {self.speed} m/s"

def get_weather_data(city, country):
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'
    
    fetch = requests.get(url)
    response = fetch.json()
    with open ('info.json', 'w') as f:
        json.dump(response, f, indent=2)    

    if 'message' in response and response['message'] == 'city not found':
            print('City not found. Please enter a valid city name.')
    elif not pycountry.countries.get(name=country.capitalize()):
        print('Country not found. Please enter a valid country code.')
        return None
    else:

        temp_data = response['main']
        temp_keys =['temp', 'feels_like', 'temp_min', 'temp_max']
        for key in temp_keys:
            if key in temp_data:
                temp_data[key] = int(temp_data[key])
        data = WeatherData(
            main = response['weather'][0]['main'],
            description = response['weather'][0]['description'],
            icon = response['weather'][0]['icon'],
            temperature = temp_data,
            speed = response['wind'].get('speed')
        )

        return data


def main():
    try:
        while True:
            city = input('City?: ').lower()
            country = input('Country?: ').capitalize()

            response = get_weather_data(city, country)

            if response:
                print(response)
                break

        response_dict = response.__dict__
        with open ('data.json', 'w') as f:
            json.dump(response_dict, f, indent=2)

    except Exception as e:
        exit(f'An error occured: \n{e}')


if __name__ == '__main__':
    main()