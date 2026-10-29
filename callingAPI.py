# pip freeze > requiremetns.txt 
import requests

# We need coordinates to get weather data
latitude = 36.8356   # Paris latitude
longitude = -1.1714   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

data ["current"]

print(data)