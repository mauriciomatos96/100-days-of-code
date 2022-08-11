import requests
from datetime import datetime

MY_LAT = 18.476280
MY_LONG = -69.983777

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]


time_now = datetime.now()

if time_now.hour >= int(sunrise):
    print("The sun just come out")
elif time_now.hour >= int(sunset):
    print("Goodbye sun")
