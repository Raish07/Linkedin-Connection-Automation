# Linkedin-Connection-Automation
This script automates the process of sending connection requests on LinkedIn using the Selenium WebDriver in Python.
Prerequisites
Python 3.x
Selenium WebDriver for Python
Chrome WebDriver (compatible with your Chrome browser version)
Installation
Install Python: Visit the Python website and follow the instructions to install Python for your operating system.

Install Selenium: Open a terminal or command prompt and run the following command to install the Selenium WebDriver for Python:


pip install selenium
**Download Chrome WebDriver: Download the Chrome WebDriver executable that matches your Chrome browser version from the ChromeDriver Downloads page. Make sure to place the WebDriver executable in a location accessible to your Python environment.**

Usage
Import the required modules:

python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
Initialize the WebDriver:

python

driver = webdriver.Chrome()
Open the LinkedIn website:

python

driver.get('https://www.linkedin.com')
Log in to your LinkedIn account:

python

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
username.send_keys('Your-LinkedIn-Username')
password.send_keys('Your-LinkedIn-Password')
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
Navigate to the search results page to find users you want to connect with:

python

driver.get("https://www.linkedin.com/search/results/PEOPLE/?keywords=ankit&network=%5B%22F%22%2C%22O%22%5D&origin=GLOBAL_SEARCH_HEADER&sid=edq")
Automate the connection request process:

python

all_buttons = driver.find_elements(By.TAG_NAME, "button")

while True:
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    if len(connect_buttons) == 0:
        break

    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

        add_note = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
        add_note.send_keys("Hii..There! I really like the work you have been doing so far. It's really inspiring to me, and that's why I would like to connect with you and learn from you. I hope you will consider my connection request and get back to me.")

        send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        send.click()

        close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)

        time.sleep(2)

        print(f"Sent connection requests to {len(connect_buttons)} users")

    next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
    if next_button.is_enabled():
        driver.execute_script("arguments[0].click();", next_button)
    else:
        break
Close the WebDriver:

python

driver.quit()
**Notes
Make sure to replace 'Your-LinkedIn-Username' and 'Your-LinkedIn-Password' in the code with your actual LinkedIn credentials.
Adjust the search results URL in Step 5 to match your desired search criteria.
Customize the connection request message in the add_note.send_keys() line to suit your requirements.
Limitations and Considerations
LinkedIn frequently updates its website, so this code may need modifications to adapt to any changes in the LinkedIn UI or structure.
Automated actions on LinkedIn may violate LinkedIn's terms of service. Use this script responsibly and ensure compliance with LinkedIn's usage policies.
LinkedIn may impose restrictions or captchas if it detects suspicious activity. Be cautious about sending too many connection requests in a short period.
Automating LinkedIn interactions may lead to account restrictions or suspensions. Use this script at your own risk.
That's it! You now have a script to automate LinkedIn connection requests using Selenium WebDriver. Happy networking!**
