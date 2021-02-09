from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def find_element_by_css_selector(root, selector, delay=10):
    try:
        element = WebDriverWait(root, delay) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException as e:
        print(e)
        element = None

    return element


if __name__ == '__main__':
    pass
