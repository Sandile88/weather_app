from flask import Flask, render_template, request
from weather import *

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home():
    data = None

    if request.method == 'POST':
        city = request.form['cityName']
        country = request.form['countryName']
        data = get_weather_data(city, country)
    return render_template('data.html', data=data)


if __name__ == '__main__':
    app.run()