import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()
user_name = driver_g.find_element(By.XPATH, '//input[@data-test="username"]')  # attribute XPATH
user_name.send_keys("standard_user")
password = driver_g.find_element(By.CSS_SELECTOR, "#password")  # css selector
password.send_keys("secret_sauce")
button_login = driver_g.find_element(By.XPATH, '//input[@value="Login"]')
time.sleep(3)
button_login.click()    #button click
# time.sleep(3)
# driver_g.close()