from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ManpowerLogin():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def teardown_method(self, method):
        self.driver.quit()

    def login_empty(self):
        self.driver.get("https://manpower.si/auth/login")
        self.driver.find_element(By.CSS_SELECTOR, ".big-button").click()
        time.sleep(2)


