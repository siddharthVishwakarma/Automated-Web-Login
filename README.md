# Automated-Web-Login
Automation project that uses Python and Selenium to automate a web login process. The project will navigate to a login page, enter credentials, and submit the form.

## How It Works
**Initialize WebDriver**: The script starts by initializing a Selenium WebDriver using ChromeDriver.
**Navigate to Login Page**: It navigates to the login page specified in config.py.
**Fill in Credentials**: The script finds the username and password fields, fills them with the provided credentials, and submits the form.
**Check Login Success**: The script checks whether the login was successful by verifying if the page title contains "Dashboard" (you can change this to match your target site).
**Close WebDriver**: Finally, the WebDriver is closed.

## Running the Script
Make sure to update the config.py file with your actual login URL, credentials, and the path to your WebDriver.
Run the script using Python
**python main.py**
