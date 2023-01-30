# 1.Авторизоваться на сайте
# 2.Выбрать 2 товара
# 3.Сохранить в переменные названия и цены товаров
# 4.Пройти весь БП, на моменте оплаты товара сверить сохраненные значения, а так же что система правильно посчитала сумму товаров (отдельно считаем сумм товаров и проверяем с тем что говорит нам система)
# 5.Не забывайте добавлять PRINT и КОММЕНТАРИИ для лучшей читаемости кода

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# environment settings for work
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\Tanya\\PycharmProjects\\TestAutomation\\chromedriver.exe')
driver_g = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver_g.get(base_url)
driver_g.maximize_window()

# authorization
login = "standard_user"
password_all = "secret_sauce"

input_login = driver_g.find_element(By.XPATH, "//input[@id='user-name']")
input_login.send_keys(login)
print("Login input - success")

input_password = driver_g.find_element(By.XPATH, "//input[@id='password']")
input_password.send_keys(password_all)
print("Password input - success")

login_button = driver_g.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Login button click - success")

# selection of products
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_1 = product_1.text  # product 1 name
print("Product 1 is: " + value_product_1)

product_1_price = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")  # такие страшные локаторы, потому что товаров 2, а в верстке называются одинаково, пришлось копировать
value_product_1_price = product_1_price.text  # product 1 price
print("Product 1 costs: " + value_product_1)

select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_1.click()
print("Add to cart product 1 - success")

product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_2 = product_2.text  # product 2 name
print("Product 2 is: " + value_product_2)

product_2_price = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
value_product_2_price = product_2_price.text  # product 2 price
print("Product 2 costs: " + value_product_2)

select_product_2 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Add to cart product 2 - success")

# go to cart
cart_button = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Go to cart - success")

# cart info
cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_cart_product_1 = cart_product_1.text
print("Product 1 in cart is: " + value_cart_product_1)

cart_product_1_price = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_product_1_price = cart_product_1_price.text
print("Costs: " + value_cart_product_1_price)

cart_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product_2 = cart_product_2.text
print("Product 2 in cart is: " + value_cart_product_2)

cart_product_2_price = driver_g.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_product_2_price = cart_product_2_price.text
print("Costs: " + value_cart_product_2_price)

# check
assert value_product_1 == value_cart_product_1
print("Product 1 is correct")
assert value_product_1_price == value_cart_product_1_price
print("Product 1 costs correctly")

assert value_product_2 == value_cart_product_2
print("Product 2 is correct")
assert value_product_2_price == value_cart_product_2_price
print("Product 2 costs correctly")

# checkout
checkout_button = driver_g.find_element(By.XPATH, "//button[@id='checkout']")
checkout_button.click()
print("Checkout button click - success")

# input info
first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("First Name")
print("Input first name - success")

last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Last Name")
print("Input last name - success")

postal_code = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys("1337")
print("Input postal code - success")

time.sleep(2)
continue_button = driver_g.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Go to checkout overview - success")

# overview



