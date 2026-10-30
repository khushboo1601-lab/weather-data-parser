from dotenv import load_dotenv
import os

def load_environment():
    """Load environment variables from the .env file."""
    load_dotenv()

def get_gemini_api_key() -> str|None:
    """Retrieve the optional Gemini API key."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    return api_key

def get_weather_api_key() -> str:
    """Retrieve the mandatory OpenWeatherMap API key."""
    weather_api_key = os.getenv("WEATHER_API_KEY")
    if not weather_api_key:
        raise ValueError("WEATHER_API_KEY not found")
    return weather_api_key