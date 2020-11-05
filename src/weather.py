# requests is used to interpret the .json data into python data
# the data is stored into python dictionaries
import requests
import yaml

# Weather Class
class Weather:

    # pull api key from secure file.
    @classmethod
    def secure_key(cls):
        with open('../config/config.yaml', 'r') as config_file:

            # safely accesses API key
            config = yaml.safe_load(config_file)

        # OpenWeatherMap API Key:
        OWM_API_KEY = config['OWM']['OWM_api_key']
        return OWM_API_KEY

    @classmethod
    def gather_info(cls, OWM_API_KEY):
        # OpenWeatherMap's URL
        url = "http://api.openweathermap.org/data/2.5/weather?"

        # Fairfax's weather of choice
        place = 'Fairfax'

        # chain variable to store
        # chain is used for OWM API
        chain = url + "appid=" + OWM_API_KEY + "&q=" + place

        # fetches chains data through requests.
        new_data = requests.get(chain)

        # Convert from json to python.
        j = new_data.json()
        return j

    @classmethod
    def get_values(cls, j):
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

        # Checks API's dictionary if rain has key
        # This certain API only includes rain within past hour
        # if it has currently rained within each hour via EST
        try:
            rain = j["rain"]
            lastHour = rain["1h"]
            lastHour = round((lastHour/25.4),2)
            rain2 = ("\n, It has rained: " + str(lastHour) + "within past hour.\n")
        # If no rain has occurred within the past hour, rain will not be a key in
        # OWM's API, therefore this error statement will state that
        # no rain has fallen within the past hour
        except:
            rain2 = ", no rain within past hour\n"
        # All weather information is placed into a string and is returned when called.
        w2 = "\n" +str(current_temperature) + "°F, " + str(weather_description) + rain2

        return w2

# below is a tester
#def main():

    #precipObj = Weather() #into class
    #OWM_API_KEY = precipObj.secure_key() #pulls from file(returns API KEY)
    #j = precipObj.gather_info(OWM_API_KEY) #pulls dictionary for weather info from API
    #w2 = precipObj.get_values(j) #stores values into strings
    #print(w2) # To see output, delete comment
    #return w2


#if __name__ == "__main__":
 #   main()
