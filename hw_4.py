import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from string import Template
from operator import contains
import array

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
# Приветствуем покупателя и отображаем каталог :) меня не было почти пол года, но я устроилась на новое место и всецело занималась адаптацией
print("Welcome to our shop!")
print("Plz select the product:")
print("id 0 - Sauce Labs Backpack")
print("id 1 - Sauce Labs Bike Light")
print("id 2 - Sauce Labs Bolt T-Shirt")
print("id 3 - Sauce Labs Fleece Jacket")
print("id 4 - Sauce Labs Onesie")
print("id 5 - Test.allTheThings() T-Shirt (Red)")
selected_product = int(input())
# я обернула все в 1 большое условие, которое сразу отметает возможность выбора несуществующего товара
if 5 >= selected_product >= 0:
    productItemName = ["4_title_link", "0_title_link", "1_title_link", "5_title_link", "2_title_link", "3_title_link",]
    productItemNameValue = Template("//a[@id='item_$productItemName']") # решила шаблонизировать XPath

    # selection of products
    product = driver_g.find_element(By.XPATH,
                                    productItemNameValue.substitute(productItemName=productItemName[selected_product]))
    value_product = product.text  # product name
    print("Product is: " + value_product)

    items_in_shop = {} # каюсь - подсмотрела такой вариант в одном из предыдущих уроков, показалось наиболее гибким.
    descriptions = driver_g.find_elements(by=By.CLASS_NAME, value='inventory_item_description')
    for desc in descriptions:
        item_name = desc.find_element(by=By.CLASS_NAME, value='inventory_item_name').text
        item_price = desc.find_element(by=By.CLASS_NAME, value='inventory_item_price').text
        items_in_shop[item_name] = item_price

    print("Product costs:" + items_in_shop.get(value_product))
    item_1 = items_in_shop.get(value_product).replace('$', '')  # сохраняем числовое значение цены товара

    productButtonName = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt",
                         "sauce-labs-fleece-jacket",
                         "sauce-labs-onesie", "test.allthethings()-t-shirt-(red)"]
    productButtonNameValue = Template("//button[@id='add-to-cart-$productButtonName']")  # шаблон для кнопки "добавить в корзину"

    select_product = driver_g.find_element(By.XPATH, productButtonNameValue.substitute(
        productButtonName=productButtonName[selected_product]))
    select_product.click()
    print("Add to cart selected product  - success")
    print("done")

    # go to cart
    cart_button = driver_g.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart_button.click()
    print("Go to cart - success")

    # cart info
    cart_product = driver_g.find_element(By.XPATH, productItemNameValue.substitute(
        productItemName=productItemName[selected_product]))
    value_cart_product = cart_product.text
    print("Product in cart is: " + value_cart_product)

    cart_product_price = driver_g.find_element(By.XPATH, "//div[contains(@class, 'inventory_item_price')][1]") # здесь будет только 1 товар, поэтому можно найти по "первому вхождению"
    value_cart_product_price = cart_product_price.text
    print("Costs: " + value_cart_product_price)
    time.sleep(3)
    # check
    assert value_product == value_cart_product
    print("Product is correct")
    assert items_in_shop.get(value_product) == value_cart_product_price
    print("Product costs correctly")

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
    finish_product = driver_g.find_element(By.XPATH, productItemNameValue.substitute(
        productItemName=productItemName[selected_product]))
    value_finish_product = finish_product.text
    print("Product in overview: " + value_finish_product)

    finish_price_product = driver_g.find_element(By.XPATH, "//div[contains(@class, 'inventory_item_price')][1]")
    value_finish_price_product = finish_price_product.text
    print("Costs: " + value_finish_price_product)

    summary_price = driver_g.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
    value_summary_price = summary_price.text
    print(value_summary_price)
    item_total = value_summary_price.replace('Item total: $', '')
    items_sum = float(item_1)

    # check
    assert value_product == value_finish_product
    print("Product in overview is the same as in cart")
    assert items_in_shop.get(value_product) == value_finish_price_product
    print("Product cost in overview is the same as in cart")
    assert float(item_total) == items_sum
    print("Summary price is correct")
    print("Smoke test - success!")
    driver_g.close()
else:
    print("Sorry, we had only products with id from 0 to 5 in our shop. Try again.")
    driver_g.close()


