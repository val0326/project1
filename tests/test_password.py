from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import pyperclip


def test_password_area_focused(driver):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    text_field.click()
    text_item = driver.find_element(By.XPATH, '//*[@for="password"]')
    assert (
        text_item.get_attribute("class")
        == "field-component__input-group field-component__input-group--fullwidth is-focused"
    )


@pytest.mark.parametrize("case", ["0", " ", "5", "-1", "&", "R", "g", "ы", "Г"])
def test_password_input_simbols(driver, case):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    text_field.send_keys(case)
    assert text_field.get_attribute("value") == case


def test_password_input_from_bufer(driver):
    driver.get("https://torgbox.ru/login")
    text_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    pyperclip.copy("Example")
    text_field.send_keys(Keys.CONTROL, "v")
    assert text_field.get_attribute("value") == "Example"


def test_password_copy_disabled(driver):
    driver.get("https://torgbox.ru/login")
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    test_password = "mySecretPassword123"
    password_field.send_keys(test_password)
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
    text_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    text_field.click()
    actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    pasted_text = text_field.get_attribute("value")
    assert pasted_text != test_password
