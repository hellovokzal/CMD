import re
from playwright.sync_api import sync_playwright
from time import sleep
import threading
import os
import random
import json
from sys import argv

#prox = argv[1]
target = 'https://www.alwaysdata.com/en/register/?d'
slist = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
         'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v' 'b', 'n' 'm']
u = random.choice(slist)
q = random.choice(slist)
r = random.choice(slist)
t = random.choice(slist)

mail = q * 4 + r * 4 + t * 4 + u * 4 +'@gmail.com'
password = u * 3 + t * 3 + r *3

pas = 'dolboeb228'
f = random.randint(1, 1000)
user = u * 3 + t * 3 + r *3

def browser(target, mail, password, pas, user):
    with sync_playwright() as p:

        browser = p.firefox.launch(
            headless=False, 
            slow_mo=50, 
            
            #proxy={
            #"server": f"http://{prox}"
            #}
            )
            
            #headless=False, 
            #slow_mo=50 
        
        pixel_2 = p.devices['Pixel 2']
        context = browser.new_context(
            locale='de-DE',
            timezone_id='Europe/Berlin',
            permissions=["geolocation"],
            #**pixel_2
        )
        
        
        page = browser.new_page()
        try:
            #print(prox)
            page.goto(target, wait_until="networkidle", timeout=15000)
            page.wait_for_timeout(3000)      
            page.fill('#id_email', mail)
            page.fill('#id_password', password)
            page.click('#id_privacy_policy')
            page.click('text=Create my profile')
            page.wait_for_timeout(3000)
            page.click('#id_contract_34')
            page.click('#id_contract_28')
            page.fill('#id_password', pas)
            page.fill('#id_name', user)
            page.click("text=Let's go!")
            page.click("text=Close")
            page.goto('https://admin.alwaysdata.com/ssh/add')
            page.fill('#id_name', user + '_' + str(f))
            page.fill('#id_password', pas)
            page.click('text=Submit')
            print(f'{user}_{f}')
            

        except Exception as a:
            print(a)
            print('fail')


browser(target, mail, password, pas, user)
