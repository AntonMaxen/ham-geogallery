import unittest
import time
from selenium import webdriver
import app.bl.user_controller as uc
from werkzeug.security import generate_password_hash
import datetime


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


class MapTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.driver = webdriver.Firefox()
        self.addCleanup(self.cleanUp)
        self.user = create_test_user()

    def cleanUp(self):
        time.sleep(1)
        self.driver.quit()

    def testMapLoad(self):
        self.driver.get(self.base_url + '/map')
        result = self.driver.execute_script(
            'return (typeof google === "object" && typeof google.maps === "object")'
        )

        self.assertTrue(result, msg="Maploading")


if __name__ == '__main__':
    remove_test_user()
    unittest.main()

