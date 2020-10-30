import requests
import yaml

place = 'Fairfax'
with open('config.yaml', 'r') as config_file:
	config = yaml.load(config_file)
	
		# OpenWeatherMap API Key:
	OWM_API_KEY = config['OWM']['OWM_api_key']

		# OpenWeatherMap's URL
	url = "http://api.openweathermap.org/data/2.5/weather?"

		# chain variable to store
		# chain is used for OWM API
	chain = url + "appid=" + OWM_API_KEY + "&q=" + place

		# fetches chains data through requests.
	new_data = requests.get(chain)

		# Convert from json to python.
	j = new_data.json()

		# Key "main" is stored to var
	var = j["main"]

		# Key "temp" is stored to current_temperature
	current_temperature = var["temp"]

		# Calculation from kelvin to farenheit
	current_temperature=(current_temperature-273)*9//5+32

		# Cast current_temp to int to remove trailing decimal and zero
	current_temperature = int(current_temperature)
		#print("\nTemperature = " +    str(current_temperature) + "°F")

		# Key "weather" is stored to k
	k = j["weather"]
			# Stores the values of the keys.
	weather_description = k[0]["description"]

	try:
		rain = j["rain"]
		lastHour = rain["1h"]
		lastHour = round((lastHour/25.4),2)
		rain2 = ("It has rained " + str(lastHour) + " inches within the past hour.")
	except:
		rain2 = "It has not rained within the past hour"


	print("\nDescription = " + str(weather_description))
	print("Temperature = " + str(current_temperature) + "°F")
	print(rain2)



