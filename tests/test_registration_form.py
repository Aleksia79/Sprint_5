import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config
from src.locators import StellarBurgersLocators
from src.helpers import generate_name_email_password

class TestStellarBurgersRegistration:

    # Регистрация с корректными данными
    def test_registration_form_correct_data_true(self, driver):
        driver.get(f'{Config.URL}register')
        name_data, email_data, password_data = generate_name_email_password()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(f'{Config.URL}login'))
        assert '/login' in driver.current_url
        # почему-то не работает в WebdriverWait выражение ниже
        # WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.AUTH_BUTTON)
        # также пробовала напрямую (ниже), но не работает
        # WebDriverWait(driver, 3).until(EC.visibility_of_element_located(By.XPATH, ".//main/div/form/button")


    # Регистрация с некорректным паролем
    def test_registration_form_incorrect_password_true(self, driver):
        driver.get(f'{Config.URL}register')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys("Александра")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys("alexdianova19111@yandeх.ru")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_FIELD).send_keys("1")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        # почему-то в моем Selenium в WebDriverWait не работают выражения 'By.' для поиска элементов
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.REGISTRATION_MESSAGE_PASSWORD))
        assert driver.find_element(*StellarBurgersLocators.REGISTRATION_MESSAGE_PASSWORD).text == 'Некорректный пароль'
        # driver.quit()
