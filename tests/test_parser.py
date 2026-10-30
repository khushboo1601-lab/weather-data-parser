import pytest
from parser import parse_weather_data

sample_weather = {
    "name": "Mumbai",
    "sys": {
        "country": "IN"
    },
    "main": {
        "temp": 30,
        "feels_like": 33,
        "humidity": 70
    },
    "weather": [
        {
            "description": "clear sky"
        }
    ],
    "wind": {
        "speed": 5
    }
}

def test_parse_weather_data_sucessful():
    result = parse_weather_data(sample_weather)

    assert result["city"] == "Mumbai"
    assert result["country"] == "IN"
    assert result["temperature"] == 30
    assert result["feels_like"] == 33
    assert result["description"] == "clear sky"
    assert result["humidity"] == 70
    assert result["wind_speed"] == 5

def test_parse_weather_data_invalid():
    with pytest.raises(ValueError):
        parse_weather_data("Mumbai")

def test_parse_weather_data_missing_fields():
    incomplete_data ={
        "city" : "Mumbai"
    }

    with pytest.raises(ValueError):
        parse_weather_data(incomplete_data)