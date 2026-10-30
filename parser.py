from typing import Dict

def parse_weather_data(data: Dict) -> Dict:
    """
    Parse the OpenWeatherMap API response and extract required weather details.

    Args:
        data: Raw weather data returned by the OpenWeatherMap API.

    Returns:
        Dict: A dictionary containing the extracted weather information.

    Raises:
        ValueError: If the input is not a dictionary or required fields are missing.
    """

    # Step 1: Validate input type
    if not isinstance(data, dict):
        raise ValueError("Weather data must be a dictionary")

    #Step 2: Validate required fields
    try:
        data["name"]
        data["sys"]["country"]
        data["main"]["temp"]
        data["main"]["feels_like"]
        data["main"]["humidity"]
        data["weather"][0]["description"]
        data["wind"]["speed"]

    except (KeyError, IndexError, TypeError):
        raise ValueError("Weather data is incomplete or invalid")

    #Step-3: Parse the data 
    parsed_data = {}
    parsed_data["city"] = data["name"]
    parsed_data["country"] = data["sys"]["country"]
    parsed_data["temperature"] = data["main"]["temp"]
    parsed_data["feels_like"] = data["main"]["feels_like"]
    parsed_data["description"] = data["weather"][0]["description"]
    parsed_data["humidity"] = data["main"]["humidity"]
    parsed_data["wind_speed"] = data["wind"]["speed"]

    return parsed_data