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
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_product_1 = product_1.text  # product 1 name
print("Product 1 is: " + value_product_1)

product_1_price = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")  # такие страшные локаторы, потому что товаров 2, а в верстке называются одинаково, пришлось копировать
value_product_1_price = product_1_price.text  # product 1 price
print("Product 1 costs: " + value_product_1_price)
item_1 = value_product_1_price.replace('$', '')  # сохраняем числовое значение цены 1 товара

select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_1.click()
print("Add to cart product 1 - success")

product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_2 = product_2.text  # product 2 name
print("Product 2 is: " + value_product_2)

product_2_price = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_product_2_price = product_2_price.text  # product 2 price
print("Product 2 costs: " + value_product_2_price)
item_2 = value_product_2_price.replace('$', '')  # сохраняем числовое значение цены 2 товара

select_product_2 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product_2.click()
print("Add to cart product 2 - success")

# go to cart
cart_button = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart_button.click()
print("Go to cart - success")

# cart info
cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_cart_product_1 = cart_product_1.text
print("Product 1 in cart is: " + value_cart_product_1)

cart_product_1_price = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_product_1_price = cart_product_1_price.text
print("Costs: " + value_cart_product_1_price)

cart_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_cart_product_2 = cart_product_2.text
print("Product 2 in cart is: " + value_cart_product_2)

cart_product_2_price = driver_g.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_product_2_price = cart_product_2_price.text
print("Costs: " + value_cart_product_2_price)

time.sleep(1)
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

time.sleep(1)
continue_button = driver_g.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Go to checkout overview - success")

# overview
finish_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_0_title_link']")
value_finish_product_1 = finish_product_1.text
print("Product 1 in overview: " + value_finish_product_1)

finish_price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_product_1.text
print("Costs: " + value_finish_price_product_1)

finish_product_2 = driver_g.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_finish_product_2 = finish_product_2.text
print("Product 2 in overview: " + value_finish_product_2)

finish_price_product_2 = driver_g.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_2 = finish_price_product_2.text
print("Costs: " + value_finish_price_product_2)

summary_price = driver_g.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)
item_total = value_summary_price.replace('Item total: $', '')
items_sum = float(item_1) + float(item_2)

# check
assert value_product_1 == value_finish_product_1
print("Product 1 in overview is the same as in cart")
assert value_product_2 == value_finish_product_2
print("Product 2 in overview is the same as in cart")
assert value_product_1_price == value_finish_price_product_1
print("Product 1 cost in overview is the same as in cart")
assert value_product_1_price == value_finish_price_product_1
print("Product 2 cost in overview is the same as in cart")
assert float(item_total) == items_sum
print("Summary price is correct")
print("Smoke test - success!")
driver_g.close()
