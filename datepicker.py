import datetime
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver_g.get(base_url)
driver_g.maximize_window()

# input date
# new_date = driver_g.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.send_keys(Keys.BACKSPACE*10)
# time.sleep(2)
# new_date.send_keys("03/01/2023")
# time.sleep(3)
# new_date.send_keys(Keys.RETURN)

# choose date
# new_date = driver_g.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.click()
# time.sleep(3)
# date_18 = driver_g.find_element(By.XPATH, "//div[@aria-label='Choose Saturday, February 18th, 2023']")
# date_18.click()

# choose today
# new_date = driver_g.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# new_date.click()
# time.sleep(3)
# date_today = driver_g.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
# date_today.click()

# choose today + 10
new_date = driver_g.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
time.sleep(3)
now_date = datetime.datetime.utcnow().strftime("%d")
print(now_date)
date = int(now_date) + 10
locator = "//div[@aria-label='Choose Monday, February " + str(date) + "th, 2023']"
print(locator)
date_today = driver_g.find_element(By.XPATH, locator)
date_today.click()

