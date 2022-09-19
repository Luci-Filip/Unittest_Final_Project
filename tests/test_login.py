import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login(unittest.TestCase):
    USERNAME = (By.XPATH,"//input[@placeholder='Username']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Password']")
    LOGIN_BUTTON =(By.XPATH,"//input[@id='login-button']")
    ERROR_MESSAGE =(By.XPATH,"//form/div/h3[@data-test='error']")
    CLICK_X_ERROR =(By.XPATH,"//h3/button")

# setUp = cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/')  # pagina de pornire

# tearDown =  cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    def test_wrong_credentials_and_inspect_messages(self):
        self.chrome.find_element(*self.USERNAME).send_keys('Texas')
        self.chrome.find_element(*self.PASSWORD).send_keys('123456789')
        sleep(3)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)
        actual_error_messages = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected_messages = "Epic sadface: Username and password do not match any user in this service"
        self.assertEqual(actual_error_messages,expected_messages, "Error messages is not correct!")

    def test_find_correct_user_pass_of_list(self):
        number_of_username_valid = 0
        possible_username = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        for i in possible_username:
            self.chrome.find_element(*self.USERNAME).clear()
            sleep(3)
            self.chrome.find_element(*self.USERNAME).send_keys(i)
            sleep(3)
            first_url = self.chrome.current_url
            self.chrome.find_element(*self.PASSWORD).clear()
            sleep(3)
            self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            sleep(3)
            last_url = self.chrome.current_url
            if last_url != first_url:
                number_of_username_valid += 1
                self.chrome.back()
        print(f'Total username are: {number_of_username_valid}')

    def test_correct_credentials(self):
        self.chrome.find_element(*self.USERNAME).send_keys('standard_user')
        self.chrome.find_element(*self.PASSWORD).send_keys('secret_sauce')
        sleep(2)
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_url = self.chrome.current_url
        expected_url = "https://www.saucedemo.com/inventory.html"
        self.assertEqual(actual_url, expected_url, "Login was not successful!")
