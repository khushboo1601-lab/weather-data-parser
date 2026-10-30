import pytest
from unittest.mock import patch
from weather_api import fetch_weather

@patch("weather_api.requests.get")
def test_mock_fetch_data(mock_get):
    sample_weather = {
        "name" : "Mumbai",
        "main" : {
            "temp" : "30"
        }
    }

    mock_get.return_value.json.return_value = sample_weather
    result = fetch_weather("Mumbai","test_123")
    assert result == sample_weather
    mock_get.assert_called_once()

@patch("weather_api.requests.get")
def test_fetch_weather_when_api_key_empty(mock_get):
    with pytest.raises(ValueError):
        fetch_weather("Mumbai","")
    mock_get.assert_not_called()


@patch("weather_api.requests.get")
def test_fetch_weather_when_city_empty(mock_get):
    with pytest.raises(ValueError):
        fetch_weather("","test_123")
    mock_get.assert_not_called()
