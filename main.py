import requests
from datetime import datetime
import smtplib

MY_LAT = round(4.071510) # Your latitude
MY_LONG = round(9.731240) # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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
hour_now = time_now.hour

#If the ISS is close to my current position


iss_latitudes_lower = round(iss_latitude - 5)
iss_latitude_higher = round(iss_latitude + 5)



if MY_LAT in range(iss_latitudes_lower, iss_latitude_higher) and hour_now >= sunset:
    my_email = "pythontestingharry@gmail.com"
    my_password = "lkpvwdrxxsfyvgbl"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="okonkwo.me1000@gmail.com", msg="Subject:ISS is over you, Look UP!! \n\n This email is to notify you that ISS is currently over you.")
        connection.close()












# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



