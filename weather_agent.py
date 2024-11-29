import os
import requests
from dotenv import load_dotenv

class WeatherAgent:
    """
    An agent that fetches and processes weather information using the OpenWeatherMap API.
    """
    
    def __init__(self):
        """Initialize the WeatherAgent with API configuration."""
        load_dotenv()
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found in environment variables")
        
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        """
        Fetch weather information for a given city.
        
        Args:
            city (str): Name of the city to get weather information for
            
        Returns:
            dict: Processed weather information
        """
        try:
            # Construct API request parameters
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use Celsius for temperature
            }
            
            # Make API call
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise exception for bad status codes
            
            # Process the response
            data = response.json()
            
            # Extract relevant information
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            
            return weather_info
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def format_weather_info(self, weather_info):
        """
        Format weather information for display.
        
        Args:
            weather_info (dict): Weather information to format
            
        Returns:
            str: Formatted weather information
        """
        if not weather_info:
            return "Unable to fetch weather information."
        
        return f"""
Weather Information for {weather_info['city']}:
Temperature: {weather_info['temperature']}°C
Humidity: {weather_info['humidity']}%
Conditions: {weather_info['description'].capitalize()}
Wind Speed: {weather_info['wind_speed']} m/s
"""

def main():
    # Create weather agent
    agent = WeatherAgent()
    
    while True:
        # Get city input from user
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Fetch and display weather information
        weather_info = agent.get_weather(city)
        print(agent.format_weather_info(weather_info))

if __name__ == "__main__":
    main()
