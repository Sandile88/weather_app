from flask import Flask, render_template, request
from weather import *
import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import os

load_dotenv()
app = Flask(__name__)
PEXELS_API_KEY = os.environ['PEXELS_API_KEY']
SEARCH_ENGINE_ID = os.environ['SEARCH_ENGINE_ID']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

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

# def background(city):
#     search_query = city

#     url = "https://googleapis.com/customsearch/v1"

#     params = {
#         "q": search_query,
#         "key": GOOGLE_API_KEY,
#         "cx": SEARCH_ENGINE_ID,
#         "searchType": "image" 
#     }

#     # url = f"https://googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={SEARCH_ENGINE_ID}&q={search_query}&searchType={searchTYpe}&imgSize=xlarge"

#     response = requests.get(url, params=params)
# # print(response.text)

#     data = response.json()['items']
# # if data['total_results'] > 0:
# #     return data['photos'][0]['src']['original']
#     # for item in data:
#     #     print(item['link'])

#     if data:
#         # print(data[0]['link'])
#         return data[1]['link']
    


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
        response.raise_for_status()  # Raises an error for bad status codes
        data = response.json()
        
        if 'items' in data and data['items']:
            # print(data['items'][0]['link'])
            return data['items'][1]['link']
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
            # background_image = get_background_images(city)
            background_image = background(city)

            # print(f"City: {city}, Country: {country}")
            # print(f"Weather Data: {weather_data_list}")
           


            if not city:
                error_message =f"City '{city}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)
            if not country:
                error_message =f"City '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)
            if weather_data_list is None:
                error_message = f"City '{city}' and country '{country}' not found. Please try again."
                return render_template('data.html',error_message=error_message, background_image=background_image)

            data = weather_data_list

        return render_template('data.html', city=city, country=country, data=data, error_message=error_message, background_image=background_image)
    except ConnectionError:
        exit('An internet connection error occured. Please try again.')


if __name__ == '__main__':
    app.run(debug=True)





