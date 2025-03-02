import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': data['name'],
            'country': data['sys']['country']
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    api_key = '0237fad26b1ddfe8ccc50e931a699c06'
    city = 'London'
    weather = get_weather(api_key, city)
    if weather:
        print(f"Current weather in {weather['city']}, {weather['country']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("Failed to get weather information")