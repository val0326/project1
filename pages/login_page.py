from pages.base_page import BasePage
from selenium.webdriver.common.by import By

login_selector = (By.XPATH, '//*[@id="email"]')
password_selector = (By.XPATH, '//*[@for="password"]')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://torgbox.ru/login")

    def login_area(self):
        return self.find(login_selector)
