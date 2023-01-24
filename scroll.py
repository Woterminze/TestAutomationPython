import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g: WebDriver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
time.sleep(5)
# driver_g.maximize_window()

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
time.sleep(3)
#driver_g.execute_script("window.scrollTo(0, 50)")
# находим элемент и наводимся (НА БОЛЬШОМ ЭКРАНЕ НЕ РАБОТАЕТ, ТАК КАК ЭЛЕМЕНТ ВИДЕН ЗАРАНЕЕ)
action = ActionChains(driver_g)
red_tshirt = driver_g.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
action.move_to_element(red_tshirt).perform()
# create screenshot
time.sleep(3)
now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") # получение текущей даты (год-месяц-число) и времени (часы-мин-сек)
screenshot_name = 'screenshot ' + now_date + '.png'
driver_g.save_screenshot('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\screen\\' + screenshot_name)  # сохранение в указанную папку
print("Screenshot create - success")