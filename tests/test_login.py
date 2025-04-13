from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import pyperclip
from pages.login_page import LoginPage


def test_login_area_focused(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_text_area()
    assert (
        login_page.result_class()
        == "field-component__input-group field-component__input-group--fullwidth is-focused"
    )


@pytest.mark.parametrize("case", ["0", " ", "5", "-1", "&", "R", "g", "ы", "Г"])
def test_login_input_simbols(driver, case):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    text_field.send_keys(case)
    assert text_field.get_attribute("value") == case


def test_login_input_from_bufer(driver):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    pyperclip.copy("Example")
    text_field.send_keys(Keys.CONTROL, "v")
    assert text_field.get_attribute("value") == "Example"


def test_login_copy_to_bufer(driver):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    text_field.send_keys("Example_two")
    element_value = text_field.get_attribute("value")
    pyperclip.copy(element_value)
    copied_element_value = pyperclip.paste()
    assert copied_element_value == element_value
