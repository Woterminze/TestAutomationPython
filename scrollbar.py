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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver_g.get(base_url)
driver_g.maximize_window()

action = ActionChains(driver_g)

slider_square = driver_g.find_element(By.XPATH, '//input[@class="slider-square"]')
action.click_and_hold(slider_square).move_by_offset(40, 0).release().perform()  # вправо +, влево -
# зажали и держим -- двигаем по оси Х на 20 -- отпустили кнопку -- сохранили сделанное
print("Yeeeeeeeeeeha")

