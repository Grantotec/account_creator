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
# Сайт http://iedem.tv
driver.get("http://iedem.tv")
# 10 секунд ожидания нужных элементов
wait = WebDriverWait(driver, 10)
# Открываем меню
wait.until(create_cond(By.CLASS_NAME, "uk-button")).click()

# Вход
wait.until(create_cond(By.CLASS_NAME, "uk-icon-sign-in")).click()

# Вводим логин и пароль
wait.until(create_cond(By.NAME, "email")).send_keys("htop000@yandex.ru")
wait.until(create_cond(By.NAME, "password")).send_keys("123Asweguh")

# Ставим галочку
wait.until(create_cond(By.ID, "checkRead")).click()

# Нажимаем войти
wait.until(create_cond(By.ID, "sbmtBtn")).click()

# Создание партнера
wait.until(create_cond(By.CLASS_NAME, "uk-button"))
driver.get("http://iedem.tv/partner/create")

# Вводим данные
wait.until(create_cond(By.NAME, "username")).send_keys(NUMBER)
wait.until(create_cond(By.NAME, "password")).send_keys(PASSWORD)
wait.until(create_cond(By.NAME, "repassword")).send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# wait.until(create_cond(By.XPATH, "//input[@type='search']"))

# Переход к рефералу
driver.get("http://iedem.tv/partner/manage/" + NUMBER)

# wait.until(create_cond(By.ID, "checkRead")).click()
# wait.until(create_cond(By.ID, "sbmtBtn")).click()

# browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
driver.switch_to.new_window("tab")
driver.get("https://10minemail.com/ru/")
time.sleep(2)
mail = wait.until(create_cond(By.CLASS_NAME, "emailbox-input opentip")).text
print(mail)


"""alert = wait.until(EC.alert_is_present())

# Store the alert text in a variable
text = alert.text

# Press the OK button
alert.accept()"""

"""mail = driver.find_element(By.XPATH, "//input[@id='mail']").get_attribute("value")
"""

"""mail = driver.
driver.switch_to.window(driver.window_handles[0])
wait.until(create_cond(By.NAME, "remark")).send_keys(Keys.CONTROL + "c")
wait.until(create_cond(By.XPATH, "//button[@type='submit']")).click()

"""

"""driver.switch_to.new_window("tab")
driver.get("https://ottplayer.tv/account/registration")
wait.until(create_cond(By.NAME, "username")).send_keys()
"""

time.sleep(100)
driver.close()