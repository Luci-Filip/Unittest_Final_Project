import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Add_to_cart(unittest.TestCase):
    USERNAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
    FLEECE_JACKET = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    BIKE_LIGHT = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    T_SHIRT = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    MY_CART = (By.XPATH, "//div[@class='shopping_cart_container'][1]")
    PRODUCTS_NUMBER = (By.XPATH, "//a[@class='shopping_cart_link']/span")
    CHECKOUT_BUTTON = (By.XPATH, "//*[@id='checkout']")

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://www.saucedemo.com/cart.html")
        self.chrome.find_element(*self.USERNAME).send_keys("standard_user")
        self.chrome.find_element(*self.PASSWORD).send_keys("secret_sauce")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def tearDown(self):
        self.chrome.quit()

    def test_add_to_cart_products(self):
        self.chrome.find_element(*self.FLEECE_JACKET).click()
        self.chrome.find_element(*self.BIKE_LIGHT).click()
        self.chrome.find_element(*self.T_SHIRT).click()
        sleep(3)
        number_of_product_cart = self.chrome.find_element(*self.PRODUCTS_NUMBER).text
        print(f'The number of products in my cart are: {number_of_product_cart}')
        self.chrome.find_element(*self.MY_CART).click()
        self.chrome.find_element(*self.CHECKOUT_BUTTON).click()
