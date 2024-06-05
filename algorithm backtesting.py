# import the selenium using pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


algo_test_url = "http://your-algotest-url.com"  # We have to  Replace it with the actual AlgoTest URL
start_time = "09:00"
time_increment = 1  
total_tabs = 60


def increment_time(current_time, minutes):
    hour, minute = map(int, current_time.split(":"))
    minute += minutes
    while minute >= 60:
        minute -= 60
        hour += 1
    return f"{hour:02d}:{minute:02d}"

# Initializing WebDriver
driver = webdriver.Chrome() 
driver.get(algo_test_url)


for i in range(total_tabs):
    if i > 0:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[i])
        driver.get(algo_test_url)

    # Increment time
    current_time = increment_time(start_time, i * time_increment)
    
    # Adjusting the time setting in the AlgoTest software
    # there's is an input field to set the time, we have to adjust the id to input field
    time_input = driver.find_element_by_id("time_input_id")  # Replace with the actual ID or selector
    time_input.clear()
    time_input.send_keys(current_time)

    # Starting the backtest
    start_button = driver.find_element_by_id("start_button_id")  # Replace it with the actual ID of start button
    start_button.click()

    time.sleep(1)  # Wait a bit for the tab to load

# Keeping the browser open for review
input("Press Enter to close the browser...")
driver.quit()
