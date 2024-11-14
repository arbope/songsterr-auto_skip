from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)  

driver.get("https://www.songsterr.com/")

while True:
    try: 
        WebDriverWait(driver, 0.01).until(
            EC.element_to_be_clickable((By.XPATH , "//a[text()='continue with interruptions']"))
        ).click()
    except Exception:
        time.sleep(0.1)