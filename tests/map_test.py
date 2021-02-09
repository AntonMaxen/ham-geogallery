import unittest
import time
from selenium import webdriver
import app.bl.user_controller as uc
import app.bl.location_controller as lc
import tests.selenium_utils as su
import tests.testdata as td
import os
from app.utils import get_project_root


class MapTestCase(unittest.TestCase):
    user, password = td.create_test_user()
    location = td.create_test_location(user)

    @classmethod
    def tearDownClass(cls):
        td.remove_test_user()
        td.remove_test_locations()

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test01_MapLoad(self):
        self.driver.get(self.base_url + '/map')
        result = self.driver.execute_script(
            'return (typeof google === "object" ' +
            '&& typeof google.maps === "object")'
        )

        self.assertTrue(result, msg="Maploading")

    def test02_MapLocation(self):
        location = MapTestCase.location
        location_id = location.Id
        self.driver.get(self.base_url + f'/map/?location_id={location_id}')
        text_container = su.find_element_by_css_selector(
            self.driver,
            '.sidebar-container.infobox > .sidebar-container-header > h4'
        )

        self.assertEqual(text_container.text, 'test-place')

    def test03_AddPicture(self):
        login_url = f'{self.base_url}/login'
        location = MapTestCase.location
        user = MapTestCase.user
        password = MapTestCase.password
        login(self.driver, login_url, user.Email, password)
        self.driver.get(f'{self.base_url}/map/?location_id={location.Id}')
        add_image_button = su.find_element_by_css_selector(
            self.driver,
            '.button-container > .info-button:nth-child(1)'
        )
        add_image_button.click()

        name_input = su.find_element_by_css_selector(
            self.driver,
            'form > input[name="image_name"]'
        )
        name_input.send_keys('test-image')
        path = os.path.join(
            get_project_root(),
            'tests',
            'files',
            'images',
            'cat.png'
        )
        file_input = su.find_element_by_css_selector(
            self.driver,
            'form > #image-browse'
        )
        file_input.send_keys(path)

        submit_button = su.find_element_by_css_selector(
            self.driver,
            'form > button'
        )

        submit_button.click()

        result = su.find_element_by_css_selector(
            self.driver,
            '.sidebar-image-group > .sidebar-image-container'
        )

        self.assertIsNotNone(result)

    def test04_AddReview(self):
        login_url = f'{self.base_url}/login'
        location = MapTestCase.location
        user = MapTestCase.user
        password = MapTestCase.password
        login(self.driver, login_url, user.Email, password)
        self.driver.get(f'{self.base_url}/map/?location_id={location.Id}')
        
        add_review_button = su.find_element_by_css_selector(
            self.driver,
            '.button-container > .info-button:nth-child(2)'
        )
        add_review_button.click()

        title_input = su.find_element_by_css_selector(
            self.driver,
            'form > input[name="title"]'
        )
        title_input.send_keys('test-title')

        review_input = su.find_element_by_css_selector(
            self.driver,
            'form > textarea[name="review_text"]'
        )
        review_input.send_keys('This is a really nice test place')

        submit_button = su.find_element_by_css_selector(
            self.driver,
            'form > button'
        )

        submit_button.click()

        review = su.find_element_by_css_selector(
            self.driver,
            '.sidebar-review-group > .sidebar-review'
        )

        self.assertIsNotNone(review)


def login(driver, url, email, password):
    driver.get(url)
    email_input = su.find_element_by_css_selector(
        driver,
        'input[name="email"]'
    )
    password_input = su.find_element_by_css_selector(
        driver,
        'input[name="password"]'
    )
    submit_button = su.find_element_by_css_selector(
        driver,
        'button.button'
    )

    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_button.click()


if __name__ == '__main__':
    unittest.main()
