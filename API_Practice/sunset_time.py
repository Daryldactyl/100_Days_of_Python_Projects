import requests
from datetime import datetime
import numpy as np
import smtplib
import time

email = "darylrobwrites@gmail.com"
password = "qqnu qvjl soww kfqx"
MY_LAT = 30.232901
MY_LONG = -90.913818

def iss_close(my_lat, my_lon, iss_lat, iss_lon):
    if np.abs(my_lat-iss_lat) <= 5 and np.abs(my_lon-iss_lon) <= 5:
        return True
    else:
        return False

def is_night(sunrise, sunset, now):
    if now < sunrise or now > sunset:
        return True
    else:
        return False

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
    'tzid': 'America/North_Dakota/Center'
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_lon = float(iss_data['iss_position']['longitude'])
iss_lat = float(iss_data['iss_position']['latitude'])


sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    if iss_close(MY_LAT, MY_LONG, iss_lat, iss_lon) and is_night(sunrise, sunset, time_now.hour):
        print('Email Sent!')
        connection = smtplib.SMTP_SSL('smtp.gmail.com')
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg='Subject:LOOK UP \n\nThe ISS is above you right now!'
                )
