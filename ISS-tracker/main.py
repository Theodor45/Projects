#!/usr/bin/env python3

import requests
import time
import smtplib
from datetime import datetime
import os


def send_email():
    with open("message.txt", 'r') as msg_file:
        message = msg_file.read()

    sender = "albertorodrigues7248@gmail.com"
    receiver = "albertorodrigues7248@gmail.com"
    password = 'cool&pass*225'

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.sendmail(
        sender,
        receiver,
        msg="Subject:ISS nearby!\n\nThe ISS is in your area. Look up!")
    connection.close()


def get_my_ip():
    ip = requests.get('https://api.ipify.org').text
    return ip


def get_my_location():
    ip = get_my_ip()
    response = requests.get(f'https://ipinfo.io/{ip}')
    data = response.json()

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    return (float(latitude), float(longitude))


def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)


#Your position is within +5 or -5 degrees of the ISS position.
location = get_my_location()
iss_location = get_iss_location()


def compare_position(you, iss):
    ur_lat = abs(int(you[0]))
    ur_lon = abs(int(you[1]))
    iss_lat = abs(int(iss[0]))
    iss_lon = abs(int(iss[1]))

    if (ur_lat - iss_lat) <= 5 and (ur_lon - iss_lon) >= -5:
        if (ur_lon - iss_lon) <= 5 and (ur_lat - iss_lon) >= -5:
            return True
        else:
            return False
    else:
        return False


os.system("touch /home/theodor/it_worked.txt")
print("ISS-tracker running!")

while True:
    if compare_position(location, iss_location) == True:
        print("ISS NEARBY")
        send_email()
        exit()
    else:
        print("ISS not nearby")
    time.sleep(60)
