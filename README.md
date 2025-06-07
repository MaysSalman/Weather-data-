# 🌤️ Simple Weather App with CSV Logging

This is a beginner-friendly Python application that retrieves and displays weather data for any city using the OpenWeatherMap API.

##  Features

- Get real-time weather data (temperature, humidity, wind speed, description)
- Log weather data with timestamps to a `CSV` file
- Emoji icons for easy interpretation of weather conditions
- Logging of events and errors to a `logfile.log`
- Simple structure with clear functions for easy learning and extension

## Tech Stack

- Python
- `requests`
- `csv`
- `datetime`
- `logging`
- `pandas` (for future data analysis)
- `matplotlib` (optional chart plotting)
  
## How to Use

1. Clone the repository
2. Replace `API_KEY` in the code with your OpenWeatherMap API key
3. Run the script and enter a city name
4. Weather info will be printed and saved to `weather_data.csv`

## Future Improvements

- Add class-based structure
- Better error handling for edge cases
- Display weather icons
- Web-based version with GUI

---

####Example Output

```bash
City: Baghdad
Weather: ☀️ clear sky
Temperature: 42.5 °C
Humidity: 9%
Wind Speed: 6.7 m/s
Time is: 2025-06-07 15:32:01
