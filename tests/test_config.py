import pytest
from config import get_weather_api_key,get_gemini_api_key

def test_get_gemini_api_key_when_available(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY","test-123")
    result = get_gemini_api_key()
    assert result == "test-123"

def test_get_gemini_api_key_when_missing(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY",raising=False)
    result = get_gemini_api_key()
    assert result == None

def test_get_weather_api_key_when_available(monkeypatch):
    monkeypatch.setenv("WEATHER_API_KEY","test-123")
    result = get_weather_api_key()
    assert result == "test-123"

def test_get_weather_api_key_when_missing(monkeypatch):
    monkeypatch.delenv("WEATHER_API_KEY",raising = False)
    with pytest.raises(ValueError):
        get_weather_api_key()