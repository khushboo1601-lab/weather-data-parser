from config import load_environment, get_weather_api_key
from weather_api import fetch_weather
from parser import parse_weather_data
from llm_client import (
    create_llm_client,
    generate_weather_recommendations
)

def main():
    """
    Run the Weather Data Parser application.
    """

    # Step 1: Load environment variables
    load_environment()

    # Step 2: Retrieve Weather API key
    weather_api_key = get_weather_api_key()

    # Step 3: Get city input
    city = input("Enter city name: ").strip()

    # Step 4: Fetch raw weather data
    raw_data = fetch_weather(city, weather_api_key)

    # Step 5: Confirm the returned city
    api_city = raw_data.get("name", "")

    if city.casefold() != api_city.casefold():
        print(f"Did you mean {api_city}?")

        confirmation = input("Enter yes or no: ").strip().casefold()

        if confirmation != "yes":
            print("Please enter the city name again.")
            return

    # Step 6: Parse weather data
    parsed_data = parse_weather_data(raw_data)

    # Step 7: Initialise Gemini client
    client = create_llm_client()

    # Step 8: Generate recommendations
    if client is not None:
        recommendation = generate_weather_recommendations(
            client, parsed_data
        )

        print("\nWeather Recommendations:")
        print(recommendation)

    else:
        print(
            "Gemini API key is unavailable. Weather data was fetched "
            "successfully, but recommendations cannot be generated."
        )


if __name__ == "__main__":
    main()