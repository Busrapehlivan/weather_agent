# Weather Agent

This project implements a Weather Agent that utilizes the OpenWeatherMap API to fetch and process weather information for different cities.

## Features
- Fetch current weather data for any city
- Display temperature, humidity, weather conditions, and wind speed
- Error handling for API requests
- Environment variable support for API key security

## Setup
1. Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/api)
2. Create a `.env` file in the project root and add your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script with:
```
python weather_agent.py
```

The agent will prompt you to enter a city name and will display the current weather information for that location.
