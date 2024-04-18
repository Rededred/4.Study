import requests


KEY = "XALGVG5AXBPXJ2K7DQ5CXH7XU"

def get_weather_by_hours_for_days_from_api(*, date: str, city: str) -> dict:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={KEY}"
    response = requests.get(url)
    return dict(response.json())

def farenheit_to_celsius(*, fareheit_temperature:float) -> int:
    return round((fareheit_temperature - 32) * 5 / 9)

[print(f'{x}: {y}') for x, y in get_weather_by_hours_for_days_from_api(date='2002-06-09', city='Kislovodsk, Russia').items()]
print('==='*15)
[print(f'{x}: {y}') for x, y in get_weather_by_hours_for_days_from_api(date='2007-09-23', city='Kislovodsk, Russia').items()]
