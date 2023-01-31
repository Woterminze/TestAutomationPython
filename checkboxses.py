import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/checkbox'
driver_g.get(base_url)
driver_g.maximize_window()

toggle_button = driver_g.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
toggle_button.click()

check_box_desktop = driver_g.find_element(By.XPATH, "//*[@class='rct-icon rct-icon-expand-close']")
check_box_desktop.click()

driver_g.find_element(By.XPATH, "//span[contains(text(),'Notes')]").click()  # более короткий формат, нажимаем на Notes


