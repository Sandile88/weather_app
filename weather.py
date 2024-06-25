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

    timestamp: str
    main: str
    description: str
    icon: str
    temperature: float
    speed: float

    def __str__(self) -> str:
        output = '\n'.join([f" {key}: {value}°C" if 'temp' or 'feel_like'  in key  else f" {key}: {value}" for key, value in self.temperature.items() if key in ['temp', 'feels_like', 'temp_min', 'temp_max']])
        symbol = icon_symbols.get(self.icon, self.icon)
        return f"""
Date: {self.timestamp}\n
Main: {self.main}, {self.description}\n 
Icon: {symbol}\n
Temperatures: \n{output}\n
Pressure: {self.temperature['pressure']}hPa\n
Humidity: {self.temperature['humidity']}% \n
Speed: {self.speed} m/s
"""


def get_weather_data(city, country):
    url= f'https://api.openweathermap.org/data/2.5/forecast?q={city},{country}&include=daily&appid={api_key}&units=metric'
    # url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}'
    
    fetch = requests.get(url)
    response = fetch.json()

    # lon = response['coord']['lon']
    # lat = response['coord']['lat']
    # print(lon, lat)
    with open ('info.json', 'w') as f:
        json.dump(response, f, indent=2)    

    # exclude = 'minutely, hourly'
    # url2 = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}'

    # fetch2 = requests.get(url2)
    # response2 = fetch2.json()

    # with open ('info2.json', 'w') as f:
    #     json.dump(response2, f, indent=2)

    

    if 'message' in response and response['message'] == 'city not found':
            print('City not found. Please enter a valid city name.')
    elif not pycountry.countries.get(name=country.capitalize()):
        print('Country not found. Please enter a valid country code.')
        return None
    else:
        weather_data_list = []
        unique_dates = set()
        for forecast in response['list']:
            date = forecast['dt_txt'][:10],
            if date not in unique_dates:
                unique_dates.add(date)
                temp_data = forecast['main']
                temp_keys =['temp', 'feels_like', 'temp_min', 'temp_max']
                for key in temp_keys:
                    if key in temp_data:
                        temp_data[key] = int(temp_data[key])

                data = WeatherData(
                    timestamp = forecast['dt_txt'][:10],
                    main = forecast['weather'][0]['main'],
                    description = forecast['weather'][0]['description'],
                    icon = forecast['weather'][0]['icon'],
                    temperature = temp_data,
                    speed = forecast['wind'].get('speed')
                )
                weather_data_list.append(data)

        return weather_data_list
    

def main():
    try:
        while True:
            city = input('City?: ').lower()
            country = input('Country?: ').lower()
            print("\nCurrent weather:")

            response = get_weather_data(city, country)

            if response:
                # duplicate_timestamps = set()
                # unique_weather_data = []
                for weather in response:
                    # if weather.timestamp not in duplicate_timestamps:
                        # unique_weather_data.append(weather)
                        # duplicate_timestamps.add(weather.timestamp)
                        print(weather)
                break

        response_dict = [weather.__dict__ for weather in response]
        with open ('data.json', 'w') as f:
            json.dump(response_dict, f, indent=2)

    except Exception as e:
        exit(f'An error occured: \n{e}')


if __name__ == '__main__':
    main()