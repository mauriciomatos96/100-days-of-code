import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 18.476280
MY_LONG = -69.983777
MY_EMAIL = "mauriciolearningpython@gmail.com"
MY_PASSWORD = "b483MM4nJD+#ZIT"
MY_PERSONAL_EMAIL = "mauriciomatos44@gmail.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

mitutes_passed = 1
while True:
    time.sleep(60)
    print(f"{mitutes_passed} minutes has passed")
    mitutes_passed += 1
    if is_night() and is_iss_overhead():
        print("se envio")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                msg=f"Subject:ISS Notifier\n\nLook Up!!\nThe ISS is above you right now",
                from_addr=MY_EMAIL,
                to_addrs=MY_PERSONAL_EMAIL)