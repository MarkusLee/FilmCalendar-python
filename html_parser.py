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

def parse_deuitkijk(html_content):
    events = []
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the section containing the film schedule
    agenda = soup.find(id='agenda')

    # Iterate through each section representing a day
    for section in agenda.find_all('section'):
        # Now, for each film showing in this section...
        for li in section.find_all('li'):
            # Extract the showing time
            datetime_str = li.find('time')['datetime']
            # Parse the time string into a datetime object
            start_datetime = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")

            start_datetime_ams = amsterdam_tz.localize(start_datetime)
            
            # Extract the film name
            film_name = li.find('span').text.strip()
            
            # Extract the link to more information
            film_info_link = 'https://www.uitkijk.nl' + li.find('a')['href']

            uid = str(uuid.uuid4())

            # combinethe ticket link and the film info link to describe the event
            description = f"Film info: {film_info_link}\n" 

            # Append the extracted data to the list
            events.append({
                'uid': uid,
                'film_name': film_name,
                'start_datetime': start_datetime,
                'description': description,
            })

    return events


def parse_kriterion(html_content):
    events = []
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the section containing the film schedule
    timetable = soup.find('div', class_='timetable')

    for day in timetable.find_all('div', class_='accordion__item'):
        # Find the accordion title to extract the date
        date_str = day.find("div", class_="timetable-accordion-title").text.strip().split()[1:]
        date_str = " ".join(date_str).replace("Mei", "May")  # TODO handle other months
        date_obj = datetime.strptime(date_str, "%d %B")
        current_year = datetime.now().year  # TODO may encounter issues in December - January

        # Iterate over each show within the accordion
        shows = day.find_all("div", class_="timetable-accordion-show")
        for show in shows:
            time = show.find("p", class_="monoFont").text
            time_obj = datetime.strptime(time, "%H:%M").time()

            film_info = show.find("a")
            film_info_link = film_info['href']
            film_name = film_info.text
            ticket_link = show.find("a", class_="accordion-ticket-link")['href']

            start_datetime = datetime(current_year, date_obj.month, date_obj.day, time_obj.hour, time_obj.minute)
            start_datetime_ams = amsterdam_tz.localize(start_datetime)

            uid = str(uuid.uuid4())

            description = f"Film info: {film_info_link}\n" \
                            f"Tickets: {ticket_link}\n"
            
            events.append({
                'uid': uid,
                'film_name': film_name,
                'start_datetime': start_datetime,
                'description': description,
            })

    return events
    

# Add more parsing functions as needed
