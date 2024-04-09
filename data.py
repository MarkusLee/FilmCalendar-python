import requests

from sites import name2url, name2parser


class Data:
    def __init__(self):
        self.data = {}

    def fetch_from_site(self, url, parser_function):
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

    def fetch(self):
        # Loop through the site_parsers dictionary and process each site
        for name, url in name2url.items():
            if name not in name2parser:
                print(f"No parser function found for {name}")
                continue
            print(f"Fetching film agenda from: {url}")
            site_data = self.fetch_from_site(url, name2parser[name])
            self.data[name] = site_data
            print("--------------------------------------------------")


