import requests, time
from requests.exceptions import RequestException


KEY = "XALGVG5AXBPXJ2K7DQ5CXH7XU"

def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f"Failed to get data. Retrying in {seconds} seconds")
                time.sleep(seconds)
        return func(*args, **kwargs)

    return wrapper_retry

@retry
def get_weather_by_hours_for_days_from_api(*, date: str, city: str) -> list[dict]:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={KEY}"
    response = requests.get(url)
    weather_by_days = response.json()["days"]
    weather_by_hours = weather_by_days[0]["hours"]
    return weather_by_hours


def farenheit_to_celsius(*, fareheit_temperature:float) -> int:
    return round((fareheit_temperature - 32) * 5 / 9)


def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather['uvindex']
        time = weather['datetime']
        celsius_temperature = farenheit_to_celsius(fareheit_temperature=weather['temp'])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celsius_temperature})

    return dangerous_hours


date = '2024-04-19'
city = 'Essentuki, Russia'
weather_by_hour = get_weather_by_hours_for_days_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hour=weather_by_hour)

[print(i) for i in dangerous_hours]