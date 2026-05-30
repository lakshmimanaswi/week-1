import urllib.request
import json

latitude = 17.3850
longitude = 78.4867

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print("\nWeather Information")
print("-" * 30)
print("Temperature:", data["current_weather"]["temperature"], "°C")
print("Wind Speed :", data["current_weather"]["windspeed"], "km/h")
print("Time       :", data["current_weather"]["time"])