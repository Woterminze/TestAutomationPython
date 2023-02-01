import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/radio-button'
driver_g.get(base_url)
driver_g.maximize_window()

radio_button = driver_g.find_element(By.XPATH, '//label[@for="yesRadio"]')
radio_button.click()

# check_box_desktop = driver_g.find_element(By.XPATH, "//*[@class='rct-icon rct-icon-expand-close']")  # типа свернуто
# check_box_desktop.click()

