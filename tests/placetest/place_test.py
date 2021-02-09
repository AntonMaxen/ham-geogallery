from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# class place_test(unittest.TestCase):


def main():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('http://127.0.0.1:5000/place')

    text_block = driver.find_element_by_class_name('username')

    search_res = WebDriverWait(driver, 10)\
        .until(EC.presence_of_element_located((By.ID, 'container')))

    result = search_res.find_elements_by_tag_name('user')

    for r in result:
        print(r.text)
        print('------')

    driver.close()




if __name__ == '__main__':
    main()
