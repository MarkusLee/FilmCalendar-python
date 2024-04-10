import requests

from sites import name2url, name2parser

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def fetch_kriterion(url, parser_function):
    options = Options()
    options.add_argument('--headless=new')
    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Wait for the JavaScript to render. You can use explicit waits or time.sleep() for simplicity
    time.sleep(5)

    html_content = driver.find_element(By.CLASS_NAME, 'timetable').get_attribute('outerHTML')

    driver.quit()

    return parser_function(html_content)


class Data:
    def __init__(self):
        self.data = {}

    def fetch_from_site(self, url, parser_function):
        # TODO improve the logic to handle different sites
        if 'kriterion' in url:
            return fetch_kriterion(url, parser_function)
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            # Call the parsing function passed as a parameter
            return parser_function(response.text)
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
            return None

    # def fetch_from_site(self, url, parser_function):
    #     # Send an HTTP GET request to the URL
    #     with open('lab111.html', 'r') as file:
    #         content = file.read()
    #     if content:
    #         # Call the parsing function passed as a parameter
    #         return parser_function(content)

    def fetch(self, sites=None):
        # Loop through the site_parsers dictionary and process each site
        if sites is None:
            sites = name2url.keys()
        for name in sites:
            url = name2url[name]
            if name not in name2parser:
                print(f"No parser function found for {name}")
                continue
            print(f"Fetching film agenda from: {url}")
            site_data = self.fetch_from_site(url, name2parser[name])
            self.data[name] = site_data
            print("--------------------------------------------------")
