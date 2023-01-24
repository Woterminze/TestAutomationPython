import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"
user_name = driver_g.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Login input - success")
user_name.send_keys(Keys.BACKSPACE)  #стирание ласт символа (нажали типа на бекспейс)
time.sleep(1)
user_name.send_keys("r")

password = driver_g.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Password input - success")
time.sleep(2)
password.send_keys(Keys.RETURN)  #Enter

# Выпадающая фильтрация
filter_product = driver_g.find_element(By.XPATH, '//select[@data-test="product_sort_container"]')
filter_product.click()
print("Click Filter- success")
time.sleep(2)
filter_product.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
# filter_product.send_keys(Keys.PAGE_DOWN)
# time.sleep(2)
filter_product.send_keys(Keys.RETURN)




# button_login = driver_g.find_element(By.XPATH, '//input[@id="login-button"]')
# button_login.click()
# print("Login button click - success")
