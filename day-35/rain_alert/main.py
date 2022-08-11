import requests
import smtplib
import os

api_key = os.environ["OWP_API_KEY"]

LAT = 18.476387
LON = -69.983621
OWP_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

MY_EMAIL = "mauriciolearningpython@gmail.com"
MY_PERSONAL_EMAIL = "mauriciomatos44@gmail.com"
MY_PASSWORD = "b483MM4nJD+#ZIT"

parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWP_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Slice solution
will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            msg="Subject:Rain\n\nToday will rain, make sure to grab your umbrella",
            from_addr=MY_EMAIL,
            to_addrs=MY_PERSONAL_EMAIL)


#My normal solution
# hour = 0
# will_rain = False
# while hour < 12:
#     condition_code = weather_data["hourly"][hour]["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#     hour += 1
#
# if will_rain == True:
#     print("Bring an Umbrella")
