from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import dotenv


dotenv.load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


def test_click_registration(driver):
    driver.get("https://torgbox.ru/login")
    link_element = driver.find_element(By.LINK_TEXT, "зарегистрируйтесь")
    link_element.click()
    assert (
        driver.find_element(
            By.XPATH,
            '//*[@class="text-center text-dark-gray hero__header hero__header--larger mb20"]',
        ).text
        == "Регистрация"
    )


def test_click_forget_password(driver):
    driver.get("https://torgbox.ru/login")
    link_element = driver.find_element(By.LINK_TEXT, "Забыли пароль?")
    link_element.click()
    assert (
        driver.find_element(
            By.XPATH, '//*[@class="text-center hero__header hero__header--larger mb20"]'
        ).text
        == "Восстановление пароля"
    )


def test_come_back_page(driver):
    driver.get("https://torgbox.ru/login")
    link_element = driver.find_element(By.LINK_TEXT, "зарегистрируйтесь")
    link_element.click()
    driver.back()
    assert (
        driver.find_element(
            By.XPATH, '//*[@class="text-center hero__header hero__header--larger mb20"]'
        ).text
        == "Вход в систему"
    )


def test_come_in_by_enter(driver):
    driver.get("https://torgbox.ru/login")
    login_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    login_field.send_keys(user)
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.staleness_of(password_field))
    current_title = driver.title
    assert current_title == "Закупки"
    hamburger_item = driver.find_element(By.XPATH, '//*[@class="hamburger__container"]')
    hamburger_item.click()
    exit_button = driver.find_element(
        By.XPATH,
        '(//button[@class="overlay-header__link overlay-header__link--button"])[1]',
    )
    exit_button.click()
