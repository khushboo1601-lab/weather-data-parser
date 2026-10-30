import requests
import json
from typing import Dict

def fetch_weather(city: str, api_key:str) -> Dict:
    """
    Fetch current weather data for a given city from OpenWeatherMap.

    Args:
        city: Name of the city for which weather data is requested.
        api_key: OpenWeatherMap API key.

    Returns:
        dict: Weather information returned by the API.

    Raises:
        ValueError: If city or API key is empty.
        requests.exceptions.RequestException: If the API request fails.
        requests.exceptions.JSONDecodeError: If the response contains invalid JSON.
    """

    #Validate input
    if not city or not city.strip():
        raise ValueError("City name cannot be empty")
    
    if not api_key or not api_key.strip():
            raise ValueError("Weather API key cannot be empty") 

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
             "q" : city,
             "appid" : api_key,
             "units" : "metric"
        }

    ##Make API request
    result = requests.get(url=base_url,params=params,timeout=10)

    #Check HTTP Response
    result.raise_for_status()

    #Parse and return JSON Response
    return result.json()