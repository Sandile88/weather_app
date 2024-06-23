from flask import Flask, render_template, request
from weather import *
import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import os

load_dotenv()
app = Flask(__name__)
PEXELS_API_KEY = os.environ['PEXELS_API_KEY']

DEFAULT_BACKGROUND_IMAGE = 'https://images.pexels.com/photos/2189696/pexels-photo-2189696.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'

def get_background_images(city):
    url = f'https://api.pexels.com/v1/search?query={city}&per_page=1'
    headers = {'Authorization': PEXELS_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    if data['total_results'] > 0:
        return data['photos'][0]['src']['original']


    return DEFAULT_BACKGROUND_IMAGE
   

# get_background_images('South Africa')


@app.route('/', methods = ['GET', 'POST'])
def home():
    try:  
        data = ""
        error_message = None
        background_image = None

        if request.method == 'POST':
            city = request.form['cityName'].lower()
            country = request.form['countryName'].lower()
            data = get_weather_data(city, country)
            background_image = get_background_images(city)


            if not city:
                error_message =f"City '{city}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)
            if not country:
                error_message =f"City '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)
            if data is None:
                error_message = f"City '{city}' and country '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)


        return render_template('data.html', data=data, error_message=error_message, background_image=background_image)
    except ConnectionError:
        exit('An internet connection error occured. Please try again.')


if __name__ == '__main__':
    app.run(debug=True)





