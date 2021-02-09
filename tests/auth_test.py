import time
import unittest
import app.bl.user_controller as uc
from selenium import webdriver

name = 'ab'


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def test_a_signup(self):
        self.driver.get('http://127.0.0.1:5000/signup')
        email_field = self.driver.find_element_by_name('Email')
        username_field = self.driver.find_element_by_name('Username')
        password_field = self.driver.find_element_by_name('Password')
        submit_button = self.driver.find_element_by_class_name('button')

        email_field.send_keys(f'{name}@mail.com')
        username_field.send_keys(name)
        password_field.send_keys(name)
        time.sleep(2)
        submit_button.click()

        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://127.0.0.1:5000/login')

    def test_b_login(self):
        self.driver.get('http://127.0.0.1:5000/login')
        email_field = self.driver.find_element_by_name('email')
        password_field = self.driver.find_element_by_name('password')
        submit_button = self.driver.find_element_by_class_name('button')

        email_field.send_keys(f'{name}@mail.com')
        password_field.send_keys(name)
        time.sleep(2)
        submit_button.click()

        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://127.0.0.1:5000/map/')

    def tearDown(self):
        uc.remove_user_by_email(f'{name}@mail.com')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
