from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


def test_login_area_focused(driver):
    driver.get("https://torgbox.ru/login")
    sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="email"]')
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform()
    element_value = driver.find_element(By.XPATH, '//*[@for="email"]')
    assert (
        element_value.get_attribute("class")
        == "field-component__input-group field-component__input-group--fullwidth is-focused"
    )
    sleep(3)


# def test_hide_placeholder(driver):
#     driver.get("https://torgbox.ru/login")
#     sleep(3)
#     element = driver.find_element(By.XPATH, '//*[@id="email"]')
#     actions = ActionChains(driver)
#     actions.move_to_element(element).click().perform()
#     element_value = driver.find_element(By.XPATH, '//*[@id="email"]')
#     assert element_value.value_of_css_property("field-component__input") == "focus"
#     sleep(3)


def test_input_simbols(driver):
    driver.get("https://torgbox.ru/login")
    sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="email"]')
    element.send_keys("5gRыГ %")
    assert element.get_attribute("value") == "5gRыГ %"
    sleep(3)
