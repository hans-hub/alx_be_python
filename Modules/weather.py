import requests
API_KEY = "c698a627f40b40d2b20100531250706"
CITY = "Accra"

def get_weather(city,api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        
        location = data['location']['name']
        region = data['location']['region']
        country = data['location']['country']
        temperature_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        feelslike_c = data['current']['feelslike_c']
        humidity = data['current']['humidity']

        print(f"Weather in {location}, {region}, {country}:")
        print(f"Temperature: {temperature_c}°C")
        print(f"Feels Like: {feelslike_c}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Unexpected response format.")


get_weather(CITY,API_KEY)