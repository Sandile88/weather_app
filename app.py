from flask import Flask, render_template, request
from weather import *
import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import os

load_dotenv()
app = Flask(__name__)
SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

DEFAULT_BACKGROUND_IMAGE = 'https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/industry/weather-forecast-background.jpg'

   
def background(city):
    search_query = city
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": search_query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "searchType": "image"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'items' in data and data['items']:
            return data['items'][0]['link']
        else:
            print("No items found in the response.")
            return DEFAULT_BACKGROUND_IMAGE
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return DEFAULT_BACKGROUND_IMAGE
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return DEFAULT_BACKGROUND_IMAGE
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")
        return DEFAULT_BACKGROUND_IMAGE




@app.route('/', methods = ['GET', 'POST'])
def home():
    try: 
        city = None
        country = None
        data = None
        error_message = None
        background_image = None

        if request.method == 'POST':
            city = request.form['cityName'].capitalize()
            country = request.form['countryName'].capitalize()
            weather_data_list = get_weather_data(city, country)
            background_image = background(city)


            if not city:
                error_message =f"City '{city}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=DEFAULT_BACKGROUND_IMAGE)
            if not country:
                error_message =f"City '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=DEFAULT_BACKGROUND_IMAGE)
            if weather_data_list is None:
                error_message = f"City '{city}' and country '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=DEFAULT_BACKGROUND_IMAGE)

            data = weather_data_list

        return render_template('data.html', city=city, country=country, data=data, error_message=error_message, background_image=background_image)
    except ConnectionError:
        exit('An internet connection error occured. Please try again.')


if __name__ == '__main__':
    app.run(debug=True)





