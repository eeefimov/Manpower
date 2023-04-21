import random

from selenium import webdriver
from selenium.webdriver.common.by import By


class ManpowerRegistration():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def teardown_method(self, method):
        self.driver.quit()

    def registration_sliders(self):
        self.driver.get("https://manpower.si/auth/login")
        self.driver.find_element(By.LINK_TEXT, "Nimate uporabniška računa? Registrirajte se tukaj").click()
        self.driver.find_element(By.NAME, "consent[1]").click()
        self.driver.find_element(By.NAME, "consent[4]").click()
        self.driver.find_element(By.NAME, "submit").click()

    def registration_form_empty(self):
        self.driver.get("https://manpower.si/auth/registration")
        self.driver.find_element(By.ID, "ontrustTrigger").click()

    def registration_form_complete(self):
        plus_str = str(random.randint(1, 100))
        self.driver.get("https://manpower.si/auth/registration")
        self.driver.find_element(By.NAME, "first_name").send_keys("testerr" + plus_str)
        self.driver.find_element(By.NAME, "last_name").send_keys("resterr" + plus_str)
        self.driver.find_element(By.NAME, "address").send_keys("earth")
        self.driver.find_element(By.NAME, "city").send_keys("dublin")
        self.driver.find_element(By.NAME, "phone").send_keys("1234567890")
        self.driver.find_element(By.NAME, "email").send_keys("tester" + plus_str + "@com.com")
        self.driver.find_element(By.NAME, "password").send_keys("123456qwerty")
        self.driver.find_element(By.NAME, "password_confirmation").send_keys("123456qwerty")
        self.driver.find_element(By.ID, "ontrustTrigger").click()
