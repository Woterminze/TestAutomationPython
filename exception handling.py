import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/dynamic-properties'
driver_g.get(base_url)
driver_g.maximize_window()

try:
    visible_button = driver_g.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
except NoSuchElementException as exception:
    print("Gotcha!")
    time.sleep(7)
    visible_button = driver_g.find_element(By.XPATH, "//button[@id='visibleAfter']")
    visible_button.click()
    print("Click visible button")