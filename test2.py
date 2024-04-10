import requests
import os

from bs4 import BeautifulSoup

from datetime import datetime

import pytz

amsterdam_tz = pytz.timezone('Europe/Amsterdam')



if os.path.exists('eye.html'):
    with open('eye.html', 'r') as file:
        html_content = file.read()
else:
    response = requests.get("https://www.eyefilm.nl/en/whats-on")
    with open('eye.html', 'w') as file:
        file.write(response.text)
    html_content = response.text
