from google import genai
from config import get_gemini_api_key
from pathlib import Path

GEMINI_MODEL_NAME = "gemini-3.5-flash-lite"

def create_llm_client():
    """
    Initialise and return the Gemini client.

    Returns:
        Gemini client if the API key is available, otherwise None.
    """
    api_key = get_gemini_api_key()
    if not api_key:
        return None
    client = genai.Client(api_key=api_key)
    return client

def load_system_prompt() -> str:
    """
    Load the system prompt from the prompt.txt file.

    Returns:
        str: The system prompt content.
    """
    prompt_path = Path(__file__).parent/"prompt.txt"
    with open(prompt_path,"r",encoding="utf-8") as file:
        system_prompt = file.read().strip()

    return system_prompt

def generate_weather_recommendations(client,weather_data):
    """
    Generate weather recommendations using Gemini.

    Args:
        client: Initialised Gemini client.
        weather_data: Parsed weather information.

    Returns:
        str: AI-generated weather recommendations.
    """

    # Step 1: Load system prompt
    prompt = load_system_prompt()

    #Step 2: Add dynamic weather info
    prompt = f"""
    {prompt}

    Current weather information:
    City: {weather_data["city"]}
    Country: {weather_data["country"]}
    Temperature: {weather_data["temperature"]}°C
    Feels like: {weather_data["feels_like"]}°C
    Description: {weather_data["description"]}
    Humidity: {weather_data["humidity"]}%
    Wind speed: {weather_data["wind_speed"]} m/s
    """

    #step 3: Send prompt to Gemini
    response = client.models.generate_content(
        model = GEMINI_MODEL_NAME,
        contents = prompt
    )

   # Step 4: Validate response
    validate_llm_response(response)

    # Step 5: Return generated recommendations
    return response.text

def validate_llm_response(response):
    """
    Validate the response received from Gemini.

    Raises:
        ValueError: If the response is None or contains empty text.
    """
    if response is None or response == " ":
        raise ValueError("Gemini returned an empty response")

    if not response.text or not response.text.strip():
        raise ValueError("Gemini response contains no text")