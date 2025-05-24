import requests
from datetime import datetime
import os
import csv
API_KEY="bea77b05b06c5dc2dd317c3803cb7d16"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
import logging

logging.basicConfig(

filename='logfile.log',

level=logging.INFO,

format='%(asctime)s - %(levelname)s - %(message)s')
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=en"
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Weather data retrieved for city: {city}")
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Error retrieving weather data for {city}: {e}")
        print("some error happened  :", e)
        return None

def weather_data(city, data):
    filename = "weather_data.csv"
    file_exists = os.path.exists(filename)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)

    #only on time
        if not file_exists:
            writer.writerow(["City", "Description", "Temperature (°C)", "Humidity(%)", "Wind_speed  (m/s)","Time"])

        # weather information
        writer.writerow([
            city.title(),
            data['weather'][0]['description'],
            data['main']['temp'],
            data['main']['humidity'],
            data['wind']['speed'],
            current_time

        ])
def get_weather_icon(description):
    description = description.lower()
    if "rain" in description:
        return "🌧️"
    elif "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "snow" in description:
        return "❄️"
    elif "storm" in description or "thunder" in description:
        return "⛈️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌈"

def display_weather_data(data):
    if data and "main" in data and "weather" in data:
        print(f"\n City: {data['name']}")
        desc = data['weather'][0]['description']
        icon = get_weather_icon(desc)
        print(f" Weather: {icon} {desc}")
        print(f" Temperature: {data['main']['temp']} °C")
        print(f" Humidity: {data['main']['humidity']}%")
        print(f" Wind Speed: {data['wind']['speed']} m/s")
        print(f" Time is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(" Weather data is not available.")

# Main program
if __name__ == "__main__":
    city = input("Enter a city name: ")
    data = get_weather(city)

    if data:
        display_weather_data(data)
        weather_data(city, data)
        print("Weather data has been saved to 'weather_data.csv'")
    else:
        print("Failed to retrieve weather data.")
