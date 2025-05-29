#!/usr/bin/env python3
import requests
import hashlib
import time
from pync import Notifier

url = "https://secure.onreg.com/onreg2/bibexchange/?eventid=6591&language=us"  
#url_mock ="https://finance.yahoo.com/quote/PLTR/?.tsrc=applewf"

def get_page_hash():
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text.strip()
        return hashlib.md5(html.encode('utf-8')).hexdigest()
    except Exception as e:
        print("Error:", e)
        return None

def notify(text):
    Notifier.notify(
        text,
        title="Page Monitor",
        open= url
    )

def monitor(interval=30):
    print("Starting marathon monitor...")
    last_hash = get_page_hash()
    while True:
        current_hash = get_page_hash()
        if current_hash != last_hash:
            notify("Page has changed")
            last_hash = current_hash
        else:
            notify(f"No change at")
        time.sleep(interval)

monitor(1800)