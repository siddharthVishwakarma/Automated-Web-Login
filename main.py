from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import config

def login_to_website():
    # Initialize the WebDriver
    service = Service(config.WEBDRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    try:
        # Navigate to the login page
        driver.get(config.LOGIN_URL)

        # Find and fill the username field
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys(config.USERNAME)

        # Find and fill the password field
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(config.PASSWORD)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Verify the login was successful
        if "Dashboard" in driver.title:
            print("Login successful!")
        else:
            print("Login failed.")

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    login_to_website()
