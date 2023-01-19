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

login_standard_user = "standard_user"
password_all = "secret_sauce"


user_name = driver_g.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Login input - success")
password = driver_g.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_all)
print("Password input - success")
button_login = driver_g.find_element(By.XPATH, '//input[@id="login-button"]')
button_login.click()
print("Login button click - success")
text_products = driver_g.find_element(By.XPATH, "//span[@class='title']")   # локатор
value_text_products = text_products.text    # считывает значение локатора
print(value_text_products)
assert value_text_products == "PRODUCTS"    # проверка, если != вылезает красная ошибка
print("End of the test_1")

url = "https://www.saucedemo.com/inventory.html"    # проверка по юрл
get_url = driver_g.current_url
print(get_url)
assert url == get_url
