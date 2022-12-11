import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_cond(by, name):
    return EC.element_to_be_clickable((by, name))


NUMBER = '9299122990'
PASSWORD = 'htophtop'

# Открываем Браузер
driver = webdriver.Chrome()
# Раскрываем на весь экран
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://10minemail.com/ru/")
time.sleep(2)
mail = wait.until(create_cond(By.CLASS_NAME, "emailbox-input opentip")).text
print(mail)