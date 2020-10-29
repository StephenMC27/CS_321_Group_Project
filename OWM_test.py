# requests is used to interpret the .json data into python data
# the data is stored into python dictionaries
import requests
import yaml

# pull api key from secure file
with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file)
    
# OpenWeatherMap API Key:
OWM_API_KEY = config['OWM']['OWM_api_key']

# OpenWeatherMap's URL
url = "http://api.openweathermap.org/data/2.5/weather?"

# Fairfax's weather of choice
place = 'Fairfax'
# chain variable to store
# chain is used for OWM API
chain = url + "appid=" + OWM_API_KEY + "&q=" + place

# fetches chains data through requests.
new_data = requests.get(chain)

# Convert from json to python
j = new_data.json()

#algorithm to fetch chance of rain
#needed seperate algorithm since API does not store this variable 
#in a easy to find place
#CURRENTLY IN THE WORKS

# Key "main" is stored to var
var = j["main"]

# Key "temp" is stored to current_temperature
current_temperature = var["temp"]

# Calculation from kelvin to farenheit
current_temperature=(current_temperature-273)*9//5+32

# Cast current_temp to int to remove trailing decimal and zero
current_temperature = int(current_temperature)

# Key "weather" is stored to k
k = j["weather"]

# Stores the values of the keys.
weather_description = k[0]["description"]

# Print temperature, description, and precipitation probability.
print("\nTemperature = " +	str(current_temperature) + "°F")
print("Description = " + str(weather_description))
