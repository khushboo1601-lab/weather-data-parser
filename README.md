# Weather Data Parser

A Python-based application that fetches weather information using the OpenWeatherMap API, parses the response, and generates weather-based recommendations using Google's Gemini API.

## Features

- Fetch weather information by city.
- Parse temperature, humidity, wind speed, and weather description.
- Generate AI-powered weather recommendations using Gemini.

## Tech Stack

- Python
- OpenWeatherMap API
- Google Gemini API
- Requests
- python-dotenv

## Project Structure

- `main.py` – Application entry point
- `weather_api.py` – Weather API integration
- `parser.py` – Weather data parsing
- `llm_client.py` – Gemini integration
- `config.py` – Configuration management

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Create a `.env` file with the required API keys.
5. Run `python main.py`.