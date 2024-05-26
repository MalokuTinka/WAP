from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
# Setup to emulate a mobile device 
mobile_emulation = { "deviceName": "Pixel 2" } 
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) 
# Initialize the WebDriver 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
 options=chrome_options) 
try:
#  Navigate to Twitch
    driver.get("https://www.twitch.tv") 
    # Click on the search icon 
    search_icon = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Search']")) 
    ) 
    search_icon.click()
    # Give an Input StarCraft II
    search_input = WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search...']")) 
    ) 
    search_input.send_keys("StarCraft II") 
    search_input.send_keys(Keys.RETURN) 

    # Scroll down 2 times 
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, window.innerHeight);") 
    time.sleep(2)
     # Select First streamer 
    streamer = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, "h4[title='ESL_SC2']")
        ) 
     ) 
    streamer.click() 
    #Wait for the streamer page to load and take a screenshot 
    WebDriverWait(driver, 20).until( EC.visibility_of_element_located((By.CSS_SELECTOR, "video")) ) 
    time.sleep(5) 
    # Wait for any potential pop-ups 
    driver.save_screenshot("streamer_page.png") 
finally:

     driver.quit()
