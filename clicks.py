import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver_g.get(base_url)
driver_g.maximize_window()

# double click
action = ActionChains(driver_g)
double_click = driver_g.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double_click).perform()

# right click
action = ActionChains(driver_g)
right_click = driver_g.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()


