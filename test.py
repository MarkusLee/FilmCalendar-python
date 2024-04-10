import time
from bs4 import BeautifulSoup
     
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Selenium to use Chrome
options = Options()
options.headless = True  # Run in headless mode (without opening a UI window)
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the web page
driver.get("https://www.kriterion.nl/")

# Wait for the JavaScript to render. You can use explicit waits or time.sleep() for simplicity
# driver.implicitly_wait(10)  # Waits for 3 seconds
time.sleep(5)
# element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "timetable"))
# )

# Now you can access the full page source
# html_content = driver.page_source
html_content = driver.find_element(By.CLASS_NAME, 'timetable').get_attribute('outerHTML')

# Close the driver
driver.quit()

# Use html_content with BeautifulSoup or another parser as needed

#output the response to file
with open('kri.html', 'w') as file:
    file.write(html_content)


# soup = BeautifulSoup(response.text, 'html.parser')

# tbody = soup.find('table', class_='agenda')



# print(tbody.prettify())
