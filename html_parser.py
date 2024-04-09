from bs4 import BeautifulSoup
from datetime import datetime
import uuid

import pytz

amsterdam_tz = pytz.timezone('Europe/Amsterdam')

def parse_lab111(html_content):
    events = []
    # Logic to parse site 1
    soup = BeautifulSoup(html_content, 'html.parser')
    agenda_table = soup.find('table', class_='agenda')

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    current_date_str = ""
    for row in soup.find('table', class_='agenda').find_all('tr'):
        # Check if the row is a date row
        if 'agenda-day' in str(row):
            current_date_str = row.find('h4').text.strip().split()[1:]
            current_date_str = " ".join(current_date_str)
            # Convert the date string to a datetime object
            date_obj = datetime.strptime(current_date_str, "%d %b %Y")
            continue  # Skip to the next row after processing a date row
        
        # Now, process the film showing rows under the current date
        time_str = row.find('td').text.strip()
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        
        # Combine the current date with the time to form a datetime object
        start_datetime = datetime.combine(date_obj.date(), time_obj)

        # TODO [NECESSARY?] Localize the datetime object to Amsterdam's timezone
        start_datetime_ams = amsterdam_tz.localize(start_datetime)
        
        film_name = row.find('td').find_next_sibling('td').text.strip()
        theatre_name = row.find('span', class_='theatre_name').text.strip()  # Extracting theatre_name

        film_info_link = row.find('td').find_next_sibling('td').find('a')['href']

        tickets_item = row.find('td', class_='w195')
        tickets_link = tickets_item.find('a')['href'] if tickets_item and tickets_item.find('a') else None

        # TODO: calculate estimated end time of the film according to the film's duration

        uid = str(uuid.uuid4())

        # combinethe ticket link and the film info link to describe the event
        description = f"Theatre: {theatre_name}\n" \
                      f"Film info: {film_info_link}\n" \
                      f"Tickets: {tickets_link}\n"

        # Append the extracted data to the list
        events.append({
            'uid': uid,
            'film_name': film_name,
            'start_datetime': start_datetime,
            'description': description,
        })
        
    return events



def parse_site_2(html_content):
    # Logic to parse site 2
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract information specific to site 2's layout
    # Return extracted data

# Add more parsing functions as needed
