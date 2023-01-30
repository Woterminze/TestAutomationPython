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


user_name = driver_g.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Login input - success")
password = driver_g.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Password input - success")
button_login = driver_g.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Login button click - success")

# Product info (1)
product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print("Product: " + value_product_1)

price_product_1 = driver_g.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print("Costs: " + value_price_product_1)

select_product_1 = driver_g.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Add to cart - success")

# Go to cart
shopping_cart = driver_g.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
shopping_cart.click()
print("Go to shopping cart - success")
time.sleep(1)
# Cart info
cart_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print("Product in cart: " + value_cart_product_1)

cart_price_product_1 = driver_g.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_cart_price_product_1 = cart_price_product_1.text
print("Costs: " + value_cart_price_product_1)

# check
assert value_product_1 == value_cart_product_1
print("Product in cart is correct")
assert value_price_product_1 == value_cart_price_product_1
print("Cost in cart is correct")

# checkout
checkout = driver_g.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
checkout.click()
print("Checkout click - success")

# input info
first_name = driver_g.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Tanya")
print("Input first name - success")

last_name = driver_g.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Koptashkina")
print("Input last name - success")

postal_code = driver_g.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys("1337")
print("Input postal code - success")

time.sleep(2)
continue_button = driver_g.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Go to checkout overview - success")

# checkout overview

finish_product_1 = driver_g.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print("Product in overview " + value_finish_product_1)

finish_price_product_1 = driver_g.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_finish_price_product_1 = finish_price_product_1.text
print("Costs: " + value_finish_price_product_1)

summary_price = driver_g.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print("Summary price: " + value_summary_price)
item_total = "Item total: " + value_finish_price_product_1
print(item_total)

# check
assert value_product_1 == value_finish_product_1
print("Product in overview is the same as in cart")
assert value_price_product_1 == value_finish_price_product_1
print("Cost in overview is the same as in cart")
assert value_summary_price == item_total
print("Summary price is the same as in overview")

time.sleep(1)

print("Smoke test - success!")
driver_g.close()
