import requests

from bs4 import BeautifulSoup
     
response = requests.get('https://www.lab111.nl/programma/listview/')

#output the response to file
with open('lab111.html', 'w') as file:
    file.write(response.text)

# print(response.text[:1000])

soup = BeautifulSoup(response.text, 'html.parser')

tbody = soup.find('table', class_='agenda')



print(tbody.prettify())
