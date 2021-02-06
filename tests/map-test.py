import unittest
import time
from selenium import webdriver
import app.bl.user_controller as uc
import app.bl.location_controller as lc
from werkzeug.security import generate_password_hash
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def remove_test_user():
    return uc.remove_user_by_username('test-username')


def create_test_user():
    password = 'test'
    hash_salt = generate_password_hash(
        password,
        method='sha256',
        salt_length=32
    )

    test_user = uc.add_user({
        'FirstName': 'test-firstname',
        'LastName': 'test-lastname',
        'Email': 'test-email@email.com',
        'Username': 'test-username',
        'Hash': hash_salt,
        'PhoneNumber': 'test-phonenumber',
        'DateOfBirth': datetime.date.fromisoformat('1996-05-29'),
        'JoinDate': datetime.date.fromisoformat('2000-01-01'),
        'PermissionLevel': 1
    })

    return test_user


def create_test_location():
    test_user = uc.get_user_by_username('test-username')
    test_location = lc.add_location({
        'Place': 'test-place',
        'Longitude': 0,
        'Latitude': 0,
        'Name': 'test-name',
        'UserId': test_user.Id
    })
    return test_location


def remove_test_locations():
    return lc.remove_locations_by_place_name('test-place')


class MapTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.driver = webdriver.Firefox()
        self.addCleanup(self.cleanUp)
        create_test_user()
        self.user = uc.get_user_by_username('test-username')
        create_test_location()
        self.location = lc.get_location_by_place_name('test-place')[0]

    def cleanUp(self):
        time.sleep(2)
        self.driver.quit()

    def testMapLoad(self):
        self.driver.get(self.base_url + '/map')
        result = self.driver.execute_script(
            'return (typeof google === "object" ' +
            '&& typeof google.maps === "object")'
        )

        self.assertTrue(result, msg="Maploading")

    def testMapLocation(self):
        location_id = self.location.Id
        self.driver.get(self.base_url + f'/map/?location_id={location_id}')
        text_container = find_element_by_css_selector(
            self.driver,
            '.sidebar-container.infobox > .sidebar-container-header > h4'
        )

        self.assertEqual(text_container.text, 'test-place')


def find_element_by_css_selector(root, selector, delay=10):
    try:
        element = WebDriverWait(root, delay) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException as e:
        print(e)
        element = None

    return element


if __name__ == '__main__':
    remove_test_user()
    remove_test_locations()
    unittest.main()
