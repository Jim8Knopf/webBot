from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://discord.gg/XqMnKuTy
sleepTime = 1.5

# PATH = 'chromedriver'
PATH = 'C:\Program Files (x86)\Chromium\Application\chrome.exe'
pdriver = webdriver.Chrome(PATH)
driver.get('https://discord.com')
time.sleep(20)

message = driver.switch_to_active_element()
message.click()

while true:
    message.send_keys('rpg hunt')
    message.send_keys(Keys.RETURN)
    time.sleep(60)

time.sleep(1)
