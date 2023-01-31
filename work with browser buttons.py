# working with hidden elements
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

# взаимодействие с скрытыми до клика элементами в меню

menu = driver_g.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(2)
print("Menu button click - success")
link_about = driver_g.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()
print("About button click - success")

driver_g.back()  # <-
print("Go back - success")
time.sleep(6)
driver_g.forward()  # ->
print("Go forward - success")  # ->
# подтверждаем успех теста по проверке url

url = "https://saucelabs.com/"    # проверка по юрл
get_url = driver_g.current_url
print(get_url)
assert url == get_url
print("End of the hidden elements test - success")
driver_g.close()
