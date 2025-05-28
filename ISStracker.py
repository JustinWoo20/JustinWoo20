import requests
from datetime import datetime, timezone
import smtplib
import time

# Insert your email, password, and smtp if using
MY_EMAIL = ""
MY_PASSWORD = ""
MAIL_SMTP = ""
MY_LAT = 40.070036657586314
MY_LONG = -86.45899866122828

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    # Compare your position with the international space station
    # Is it within 5 degrees
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

# Change your tzid based on your location
def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    your_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    your_response.raise_for_status()
    data = your_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = datetime.now(timezone.utc).hour
    if current_hour < sunrise or current_hour > sunset:
        return True

while True:
    time.sleep(300)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(MAIL_SMTP)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up!\n\nThe ISS is above you right now. Look into the sky."
        )
