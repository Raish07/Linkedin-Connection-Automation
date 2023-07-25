from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open LinkedIn website
driver.get('https://www.linkedin.com')

# Maximize the window
driver.maximize_window()

# Implicitly wait for elements to be found
driver.implicitly_wait(20)

# LOG IN

# Find the username input field
username = driver.find_element(By.XPATH, "//input[@name='session_key']")

# Find the password input field
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

# Enter the username and password
username.send_keys('gbvq3aqxw@wuuvo.com')
password.send_keys('')

# Pause for 2 seconds
time.sleep(2)

# Find the submit button and click it
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()


# ADD CONTACT

# Go to the search results page for the keyword "ankit" and specific network filters
driver.get("https://www.linkedin.com/search/results/PEOPLE/?keywords=vikas&network=%5B%22F%22%2C%22O%22%5D&origin=GLOBAL_SEARCH_HEADER&sid=X~0")

# Pause for 2 seconds
time.sleep(2)

# Find all the buttons on the page
all_buttons = driver.find_elements(By.TAG_NAME, "button")

# Loop until there are no more "Connect" buttons
while True:
    # Find all the "Connect" buttons on the page
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    # If no "Connect" buttons are found, exit the loop
    if len(connect_buttons) == 0:
        break

    # Iterate over each "Connect" button and send connection requests
    for btn in connect_buttons:
        # Click the "Connect" button using JavaScript
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

        # Find the "Add a note" button and enter a note
        add_note = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
        add_note.send_keys("Hii..There! I really like the work you have been doing so far. It's really inspiring to me, and that's why I would like to connect with you and learn from you. I hope you will consider my connection request and get back to me.")

        # Find the "Send now" button and click it to send the connection request
        send = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
        send.click()

        # Find the "Dismiss" button and click it to close the confirmation dialog
        close = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)

        # Pause for 2 seconds
        time.sleep(2)

        # Print the number of connection requests sent
        print(f"Sent connection requests to {len(connect_buttons)} users")

    # Find the "Next" button and click it if it is enabled
    next_button = driver.find_element(By.XPATH, "//button[@aria-label='Next']")
    if next_button.is_enabled():
        driver.execute_script("arguments[0].click();", next_button)
    else:
        break

# Quit the WebDriver and close the browser
driver.quit()
