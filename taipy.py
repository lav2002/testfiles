from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests

def take_screenshot(url, output_file):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

    # Set up the Chrome webdriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the given URL
        driver.get(url)
        
        # Wait for some time to let the page load completely
        time.sleep(5)

        # Take a screenshot of the entire webpage
        driver.save_screenshot(output_file)

    finally:
        # Close the webdriver
        driver.quit()

def send_screenshot_to_php(screenshot_path, php_endpoint):
    # Prepare files for POST request
    files = {'screenshot': open(screenshot_path, 'rb')}

    # Make a POST request to the PHP file
    response = requests.post(php_endpoint, files=files)

    # Print the response from the server
    print(response.text)

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    screenshot_output = "screenshot.png"
    php_endpoint = "http://example.com/upload.php"  # Replace with your PHP file endpoint

    take_screenshot(website_url, screenshot_output)
    send_screenshot_to_php(screenshot_output, php_endpoint)
