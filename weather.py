import requests
import json
import os
from dotenv import load_dotenv
from dataclasses import dataclass
# from flask import Flask, render_template, request


# app = Flask(__name__)
load_dotenv()

@dataclass
class WeatherData:
    city_name: str
    country: str
    main: str
    description: str
    icon: str
    temperature: float
    speed: float


# @app.route('/')
# def home():
#     return render_template('data.html')


# @app.route(methods = ['POST'])
def get_weather_data(city):
    api_key = os.environ['API_KEY']    
    # city = request.form['information']
    # url= f'https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    fetch = requests.get(url)
    response = fetch.json()
    
    if 'message' in response and response['message'] == 'city not found':
        return None
    else:
        return response

# @app.route('get_weather_information')
def main():
    try:
        while True:
            city = input('Enter City: ')
            # country_code = input('Enter Country: ')

            response = get_weather_data(city)


            if response:
                break
            else:
                print('City not found. Please enter a valid city name.')

        data = WeatherData(
            city_name = response.get('name'),
            country = response.get('sys').get('country'),
            main = response['weather'][0]['main'],
            description = response['weather'][0]['description'],
            icon = response['weather'][0]['icon'],
            temperature = response['main'],
            speed = response['wind'].get('speed')
        )

        with open ('data.json', 'w') as f:
            json.dump(response, f, indent=2)
        return data

        # print(city_name, country, weather, weather_description, weather_icon, temperature, wind)

        # print('\nWeather report: ')
        # print(f'Area: {city_name}, {country}')
        # print(f'Weather: {weather}')
        # print(f'Description: {weather_description}')
        # print('Temperature: ')
        # for key, value in temps.items():
        #     if key != 'pressure' and key != 'humidity':
        #         print(f'{" " * 12}{key}: {value - 273.15:.1f}°C')
        #     if key == 'pressure':
        #         print(f'{" " * 12}{key}: {value}hPa')
        #     if key == 'humidity':
        #         print(f'{" " * 12}{key}: {value}%')



        # print('Wind:')
        # for key, value in wind.items():
        #     if key == 'speed':
        #         print(f'{" " * 5}{key}: {value}m/s')
        #     if key == 'deg':
        #         print(f'{" " * 5}{key}: {value}°')

    
        # with open ('data.json', 'w') as f:
        #     json.dump(response, f, indent=2)
    except Exception as e:
        exit(f'An error occured: \n{e}')

    # return render_template('data.html', information=data)

if __name__ == '__main__':
    print(main())