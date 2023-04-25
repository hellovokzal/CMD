import requests
import time
secound = 0
minute = 0
hour = 0
day = 0
while True:
    active = f"{day}:{hour}:{minute}:{secound}"
    url = "https://time-6ceaf-default-rtdb.firebaseio.com/messages.json"
    requests.post(url, json=active)
    print(active)
    time.sleep(1)
    secound = secound + 1
    if secound == 60:
        secound = 0
        minute = minute + 1
    if minute == 60:
        secound = 0
        minute = 0
        hour = hour + 1
    if hour == 24:
        secound = 0
        minute = 0
        hour = 0
        day = day + 1 
