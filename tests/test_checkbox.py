from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_checkbox_is_off(driver):
    driver.get("https://torgbox.ru/login")
    checkbox_field = driver.find_element(By.XPATH, '//*[@id="alien-computer"]')
    assert checkbox_field.get_attribute("value") == "false"


def test_checkbox_set_by_mouse(driver):
    driver.get("https://torgbox.ru/login")
    checkbox_field = driver.find_element(By.XPATH, '//*[@for="alien-computer"]')
    checkbox_field.click()
    checkbox_field = driver.find_element(By.XPATH, '//*[@id="alien-computer"]')
    assert checkbox_field.get_attribute("value") == "true"


def test_checkbox_remove_by_mouse(driver):
    driver.get("https://torgbox.ru/login")
    checkbox_field = driver.find_element(By.XPATH, '//*[@for="alien-computer"]')
    actions = ActionChains(driver)
    actions.move_to_element(checkbox_field).click().click().perform()
    checkbox_field = driver.find_element(By.XPATH, '//*[@id="alien-computer"]')
    assert checkbox_field.get_attribute("value") == "false"


def test_checkbox_set_by_space(driver):
    driver.get("https://torgbox.ru/login")
    element = driver.find_element(By.TAG_NAME, "body")
    element.send_keys(Keys.TAB * 3)
    checkbox_field = driver.find_element(By.XPATH, '//*[@id="alien-computer"]')
    checkbox_field.send_keys(Keys.SPACE)
    assert checkbox_field.get_attribute("value") == "true"


def test_checkbox_remove_by_space(driver):
    driver.get("https://torgbox.ru/login")
    checkbox_field = driver.find_element(By.XPATH, '//*[@for="alien-computer"]')
    checkbox_field.click()
    element = driver.find_element(By.TAG_NAME, "body")
    element.send_keys(Keys.TAB * 3)
    checkbox_field = driver.find_element(By.XPATH, '//*[@id="alien-computer"]')
    checkbox_field.send_keys(Keys.SPACE)
    assert checkbox_field.get_attribute("value") == "false"
