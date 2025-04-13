from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_transfer_email_(driver):
    driver.get("https://torgbox.ru/login")
    email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    email_field.send_keys("myEmail@mail.com")
    forget_link = driver.find_element(By.LINK_TEXT, "Забыли пароль?")
    forget_link.click()
    email_field2 = driver.find_element(By.XPATH, '//*[@id="login"]')
    assert (
        email_field2.get_attribute("value") == "myEmail@mail.com"
    ), "E-mail не переносится в поле восстановления пароля"


def test_back_from_forget_password(driver):
    driver.get("https://torgbox.ru/login")
    element = driver.find_element(By.LINK_TEXT, "Забыли пароль?")
    element.click()
    new_element = driver.find_element(
        By.XPATH, '//*[@class="text-center hero__header hero__header--larger mb20"]'
    )
    driver.back()
    WebDriverWait(driver, 10).until(EC.staleness_of(new_element))
    current_title = driver.title
    assert (
        current_title == "Авторизация"
    ), "Возврат происходит не на страницу авторизации"
