from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)  

def skipInterruptions():
    while True:
        try: 
            WebDriverWait(driver, 0.01).until(
                EC.element_to_be_clickable((By.XPATH , "//a[text()='continue with interruptions']"))
            ).click()
        except Exception:
            time.sleep(0.5)

def goToMainDomain():
    while True:
        try: 
            WebDriverWait(driver, 0.01).until(
                EC.element_to_be_clickable((By.XPATH , "/html/body/div[1]/div[2]/div/a"))
            ).click()
        except Exception:
            time.sleep(1)

while True:
    if driver.current_url[0:26] == "https://www.songsterr.com/":
        skipInterruptions()
    if driver.current_url == "https://dominioshdfull.com/":
        goToMainDomain()