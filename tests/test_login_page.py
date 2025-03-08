import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.config import Config
from src.locators import StellarBurgersLocators

class TestStellarBurgersLogin:
    # фикстура для класса TestStellarBurgersLogin для старта тестов с главной страницы
    @pytest.fixture(autouse=True)
    def main_page(self, auth_driver):
        WebDriverWait(auth_driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_LOGIN_PAGE))
        return auth_driver.get(Config.URL)

    # авторизация с корректным заполненинием полей
    def test_autorization_with_correct_data_true(self, auth_driver):
         assert auth_driver.current_url == Config.URL

    # переход по клику на «Личный кабинет» с главной страницы для авторизованного пользователя
    def test_switch_to_auth_account_page_true(self, auth_driver):
         auth_driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_PAGE).click()
         assert '/account/profile' in auth_driver.current_url

    # переход из личного кабинета по клику на «Конструктор» для авторизованного пользователя
    def test_click_on_constructor_from_auth_account_true(self, auth_driver):
         auth_driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_PAGE).click()
         auth_driver.find_element(*StellarBurgersLocators.LINK_TO_CONSTRUCTOR).click()
         assert auth_driver.current_url == Config.URL

    # переход из личного кабинета по клику на логотип Stellar Burgers для авторизованного пользователя
    def test_click_on_logo_from_auth_account_true(self, auth_driver):
         auth_driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_PAGE).click()
         auth_driver.find_element(*StellarBurgersLocators.LINK_TO_LOGO).click()
         assert auth_driver.current_url == Config.URL

    # выход по кнопке «Выйти» в личном кабинете
    def test_exit_from_auth_account_true(self, auth_driver):
         auth_driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_PAGE).click()
         WebDriverWait(auth_driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.BUTTON_EXIT_FROM_ACCOUNT))
         auth_driver.find_element(*StellarBurgersLocators.BUTTON_EXIT_FROM_ACCOUNT).click()
         WebDriverWait(auth_driver, 3).until(EC.visibility_of_element_located(StellarBurgersLocators.AUTH_BUTTON))
         assert 'login' in auth_driver.current_url

