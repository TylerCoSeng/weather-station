import pytest
from weather_station import WeatherStation

def test_collect_data_range():
    ws = WeatherStation()
    reading = ws.collect_data()
    assert 15.0 <= reading['temperature'] <= 30.0
    assert 30.0 <= reading['humidity'] <= 70.0
    assert 1000 <= reading['pressure'] <= 1025

def test_store_data():
    ws = WeatherStation()
    r = {'temperature': 20.0, 'humidity': 50.0, 'pressure': 1010}
    ws.store_data(r)
    assert ws.data[-1] == r

def test_analyze_data_empty():
    ws = WeatherStation()
    assert ws.analyze_data() is None

def test_analyze_data_avg():
    ws = WeatherStation()
    ws.data = [{'temperature': 20.0}, {'temperature': 30.0}]
    result = ws.analyze_data()
    assert result['average_temperature'] == 25.0