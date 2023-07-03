from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver_g.get(base_url)
driver_g.maximize_window()

# клик и очистка поля для ввода даты
new_date = driver_g.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
new_date.send_keys(Keys.BACKSPACE * 10)
time.sleep(3)
print("Cleaning ...")

# получение текущей даты в нужном формате (сайт требует слэши)
current_date = datetime.today()
current_date_string = current_date.strftime('%m/%d/%Y')
# текущая дата + 10 дней
future_date = datetime.today() + timedelta(days=10)
future_date_format = future_date.strftime('%m/%d/%Y')

print("Прибавили к текущей дате 10 дней и привели к формату, нужному на сайте...")
print("Как же я долго не могла додуматься до оптимального решения, Вы бы знали))")

new_date.send_keys(future_date_format)
print("Test - success!!!")
time.sleep(5)
driver_g.close()

