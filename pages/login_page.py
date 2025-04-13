from pages.base_page import BasePage
from selenium.webdriver.common.by import By

login_selector = (By.XPATH, '//*[@id="email"]')
login_result_selector = (By.XPATH, '//*[@for="email"]')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("https://torgbox.ru/login")

    def text_area(self):
        return self.find(login_selector)

    def click_text_area(self):
        self.text_area().click()

    def result_area(self):
        return self.find(login_result_selector)

    def result_class(self):
        return self.result_area().get_attribute("class")
