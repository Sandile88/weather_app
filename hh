Consider the following:
first css:

:root {
  --white: #ffffff;
  --off-white: #e5e5e5;
  --transp-white-1: rgba(255, 255, 255, 0.25);
  --transp-white-2: rgba(255, 255, 255, 0.18);
  --blue-1: #62b8f5;
  --blue-2: #4475ef;
  --shadow: rgba(3, 46, 87, 0.2);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.container {
  width: 50%;
  background: var(--transp-white-2);
  backdrop-filter: blur(10px);
  margin: auto;
  padding: 2rem;
  border: 2px solid var(--transp-white-2);
  border-radius: 10px;
  color: rgb(5,41,51);
  height: auto;
}

input, .btn::placeholder {
  background-color: transparent;
  padding: .5rem;
  border-radius: 10px;
  outline: none;
  border: 1px solid white;
}

.btn {
  padding: .5rem 1rem;
  border: 2px solid #04009A;
  cursor: pointer;
  transition: .3s;
  color: var(--blue-2);
  background-color: transparent;
  border-radius: 0.3em;
}

.btn:hover {
  transform: translateY(-3px);
  background-color: rgb(5,41,51);
  color: #fff;
}


.current-weather {
  background: var(--transp-white-1);
  backdrop-filter: blur(10px);
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 1rem;
  box-shadow: 0 0 10px var(--shadow);
  border: 2px solid var(--blue-2);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 400px;
  height: 555px;
}


.current-weather .header-row {
  height: 22px;
  font-size: 14px;
  line-height: 22px;
  font-weight: 600;
  justify-content: flex-start;
  white-space: nowrap;
  overflow: hidden;
}

.current-weather .content {
  display: flex;
  justify-content: space-between;
  /* margin-top: 0.5rem; */

}

.left-section, .right-section {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.left-section h2 {
  font-size: 18px;
  font-weight: 600;

}

.right-section .right-w {
  text-transform: capitalize;
}


 .weather-cards {
  display: flex;
  gap: 20px;
  flex-direction: row;
  padding: 1rem;
}

.weather-cards .card {
  list-style: none;
  padding: 18px 16px;
  border-radius: 5px;
  width: calc(100% / 5);
  align-items: center;
  /* background: var(--transp-white-3);  */
  
  background: var(--transp-white-1);
  border: 2px solid var(--blue-2);
  text-transform: capitalize;



  backdrop-filter: blur(10px);


}

.weather-cards .card img {
  margin-bottom: 10px;
  max-width: 70px;
  margin: 5px 0 -12px 0;
}

body {
  background-image: url("https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/industry/weather-forecast-background.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
}

/* small devs */
@media(min-width: 300px){
  .container{
      width: 70vw;
      height: 70vh;
  }

  .col-auto{
      margin: 1rem;
  }

  .left{
      margin: 1rem;
  }
}

second css:

:root {
    --white: #ffffff;
    --off-white: #e5e5e5;
    --transp-white-1: rgba(255, 255, 255, 0.25);
    --transp-white-2: rgba(255, 255, 255, 0.18);
    --blue-1: #62b8f5;
    --blue-2: #4475ef;
    --shadow: rgba(3, 46, 87, 0.2);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

.container {
    width: 50%;
    background: var(--transp-white-2);
    backdrop-filter: blur(10px);
    margin: auto;
    padding: 2rem;
    border: 2px solid var(--transp-white-2);
    border-radius: 10px;
    color: rgb(5,41,51);
    height: auto;
}

input, .btn::placeholder {
    background-color: transparent;
    padding: .5rem;
    border-radius: 10px;
    outline: none;
    border: 1px solid white;
}

.btn {
    padding: .5rem 1rem;
    border: 2px solid #04009A;
    cursor: pointer;
    transition: .3s;
    color: var(--blue-2);
    background-color: transparent;
    border-radius: 0.3em;
}

.btn:hover {
    transform: translateY(-3px);
    background-color: rgb(5,41,51);
    color: #fff;
}

.weather-container {
    margin-top: 2rem;
}

.current-weather, .forecast-day {
    background: var(--transp-white-1);
    backdrop-filter: blur(10px);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1rem;
    box-shadow: 0 0 10px var(--shadow);
}

.current-weather {
    border: 2px solid var(--blue-2);
}

.forecast-day {
    border: 1px solid var(--blue-1);
}

body {
    background-image: url("https://www.metoffice.gov.uk/binaries/content/gallery/metofficegovuk/hero-images/advice/industry/weather-forecast-background.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

for the above, please adjust thesize of the first css container to the size of the second css.

below is my html file:

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" 
    crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles/styles.css') }}">
</head>
<body class="text-white" {% if background_image %} style="background-image: url('{{ background_image }}')" {% endif %}>
    <div class="text-center">
        <h1 class="mt-5">Weather Report</h1>
        <form action="/" method="post" class="mt-4">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-auto">
                        <input type="text" id="cityName" name="cityName" placeholder="City" class="form-control">
                    </div>
                    <div class="col-auto">
                        <input type="text" id="countryName" name="countryName" placeholder="Country" class="form-control">
                    </div>
                    <div class="col-auto">
                        <button class="btn btn-light">Find</button>
                    </div>
                </div>
            </div>
        </form>

        <div class="mt-4">
            {% if error_message %}
              <p>{{ error_message }}</p>
            {% endif %}
        </div>

        {% if data %}
        <div class="current-weather">
            <div class="header-row">Current weather
                <div class="content">
                    <div class="left-section">
                        <div class="left-w">
                            <h2>{{ data[0].timestamp }}</h2>
                        </div>
                        <div class="left-d">
                            <p>Feels like: {{ data[0].temperature['feels_like'] }}°C</p>
                            <p>Max temp: {{ data[0].temperature['temp_max'] }}°C</p>
                            <p>Min temp: {{ data[0].temperature['temp_min'] }}°C</p>
                        </div>
                    </div>
                    <div class="right-section">
                        <div class="right-w">
                            <p>Main: {{ data[0].main }}, {{ data[0].description }}</p>
                            <img src="https://openweathermap.org/img/wn/{{ data[0].icon }}@2x.png" alt="Weather Icon">
                        </div>
                        <div class="right-d">
                            <p>Pressure: {{ data[0].temperature['pressure'] }}hPa</p>
                            <p>Humidity: {{ data[0].temperature['humidity'] }}%</p>
                            <p>Speed: {{ data[0].speed }} m/s</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="forecast mt-4">
            <ul class="weather-cards">
            {% for day in data[1:] %}
                <li class="card">
                    <h3>{{ day.timestamp }}</h3>
                    <p>Main: {{ day.main }}, {{ day.description }}</p>
                    <img src="https://openweathermap.org/img/wn/{{ day.icon }}@2x.png" alt="Weather Icon">
                    <p>Temp: {{ day.temperature['temp'] }}°C</p>
                    <p>Humidity: {{ day.temperature['humidity'] }}%</p>
                    <p>Speed: {{ day.speed }} m/s</p>
                </li>
            {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" 
    crossorigin="anonymous"></script>
</body>
</html>

also the conatiner that is storing my  current weather isn't diplsaying anything. why?