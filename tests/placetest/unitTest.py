from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import app.bl.location_controller as lc
from app.data.models.location import Location
from app.data.db import *


class place_test(unittest.TestCase):
    def setUp(self):
        self.url = ''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.location = session.query(Location). \
            filter(Location.Place.like(f'%{self.url}%')).all()

    def test_user(self):

        self.driver.get(f'http://127.0.0.1:5000/place/{self.url}')

        users = []
        search_res = WebDriverWait(self.driver, 10) \
            .until(EC.presence_of_element_located((By.ID, 'container')))

        test_users = [item.text for item in
                      search_res.find_elements_by_tag_name('user')]

        loc_list = [item.review for item in self.location]
        for rev in loc_list:
            for username in rev:
                users.append(username.user.Username)

        for user in users:
            self.assertIn(user, test_users)

    def test_goto_map(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
