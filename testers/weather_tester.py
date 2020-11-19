#Test file

import requests
import yaml

j = []
w2 = None

# Creates a list of various data inputs for weather.
def gather_info():
	global j
	j.append({})

	j.append({'coord': {'lon': -77.35, 'lat': 38.85}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 284.03, 'feels_like': 277.63, 'temp_min': 283.15, 'temp_max': 284.82, 'pressure': 1032, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 190}, 'clouds': {'all': 75}, 'dt': 1605813694, 'sys': {'type': 1, 'id': 4481, 'country': 'US', 'sunrise': 1605787025, 'sunset': 1605822785}, 'timezone': -18000, 'id': 4758041, 'name': 'Fairfax', 'cod': 200})

	j.append({'coord': {'lon': -77.35, 'lat': 38.85}, 'weather': [{'id': 803, 'main': 'Clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 284.03, 'feels_like': 277.63, 'temp_min': 283.15, 'temp_max': 284.82, 'pressure': 1032, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 190}, 'clouds': {'all': 75}, 'dt': 1605813694, 'sys': {'type': 1, 'id': 4481, 'country': 'US', 'sunrise': 1605787025, 'sunset': 1605822785}, 'timezone': -18000, 'id': 4758041, 'name': 'Fairfax', 'cod': 200})

	j.append({'coord': {'lon': -77.35, 'lat': 38.85}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 190}, 'clouds': {'all': 75}, 'dt': 1605813694, 'sys': {'type': 1, 'id': 4481, 'country': 'US', 'sunrise': 1605787025, 'sunset': 1605822785}, 'timezone': -18000, 'id': 4758041, 'name': 'Fairfax', 'cod': 200})

	j.append({'coord': {'lon': -77.35, 'lat': 38.85}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 284.03, 'feels_like': 277.63, 'temp_min': 283.15, 'temp_max': 284.82, 'pressure': 1032, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 190}, 'clouds': {'all': 75}, 'dt': 1605813694, 'sys': {'type': 1, 'id': 4481, 'country': 'US', 'sunrise': 1605787025, 'sunset': 1605822785}, 'timezone': -18000, 'id': 4758041, 'name': 'Fairfax', 'cod': 200})

	j.append({'coord': {'lon': -77.35, 'lat': 38.85}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 284.03, 'feels_like': 277.63, 'temp_min': 283.15, 'temp_max': 284.82, 'pressure': 1032, 'humidity': 37}, 'visibility': 10000, 'wind': {'speed': 5.7, 'deg': 190}, 'rain': {'1h': 4.01}, 'clouds': {'all': 75}, 'dt': 1605813694, 'sys': {'type': 1, 'id': 4481, 'country': 'US', 'sunrise': 1605787025, 'sunset': 1605822785}, 'timezone': -18000, 'id': 4758041, 'name': 'Fairfax', 'cod': 200})


def get_values(j):
	#The following try/except blocks check if a data input is not present
    #If a data input is not present, the user testing the file will be prompted.
	# Same logic present in the weather.py file. Until the main function.
    try:
        var=j["main"]
        current_temperature = var["temp"]
        current_temperature=(current_temperature-273)*9//5+32
        current_temperature = int(current_temperature)
    except:
        current_temperature = ("Error with temp data")

    try:
        k = j["weather"]
        weather_description = k[0]["description"]
    except:
        weather_description = ("Error with description data")

    try:
        rain = j["rain"]
        lastHour = rain["1h"]
        lastHour = round((lastHour/25.4),2)
        rain2 = (",\nit has rained: " + str(lastHour) + " inches within the hour.\n")

    except:
        rain2 = ", no rain within past hour\n"

    w2 = "\n" +str(current_temperature) + "°F, " + str(weather_description) + rain2

    print(w2)


# Main function
def main():
    i=0
    gather_info()
    for i in range(len(j)):
        get_values(j[i])
        i+=1



if __name__ == '__main__':
	main()

