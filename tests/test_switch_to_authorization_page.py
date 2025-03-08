import pytest

from src.config import Config
from src.locators import StellarBurgersLocators

class TestStellarBurgersAuthorization:

    # пыталась сделать с параметризацией, но не получается

    # переход на страницу авторизации:
    # по кнопке "Войти в аккаунт" на главной странице,
    # по кнопке "Личный кабинет" на главной странице
    # по кнопке "Войти" на странице регистрации,
    # по кнопке "Войти" на странице восстановления пароля
    # @pytest.mark.parametrize('page,button', [
    #     (Config.URL, StellarBurgersLocators.BUTTON_LOGIN_TO_ACCOUNT),
    #     (Config.URL, StellarBurgersLocators.BUTTON_LOGIN_PAGE),
    #     (f'{Config.URL}register', StellarBurgersLocators.LINK_LOGIN_FROM_REGISTRATION),
    #     (f'{Config.URL}forgot-password', StellarBurgersLocators.LINK_LOGIN_FROM_PASSWORD_RECOVERY)
    # ])
    # def test_negative_add_book_in_favorites_true(self, driver, page, button):
    #     driver.get(page)
    #     driver.find_element(button).сlick()
    #     assert 'login' in driver.current_url

    # переход на страницу авторизации по кнопке "Войти в аккаунт"
    def test_switch_to_authorization_button_login_to_account_true(self, driver):
         driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_TO_ACCOUNT).click()
         assert 'login' in driver.current_url


    # переход на страницу авторизации по кнопке "Личный кабинет" на главной странице
    def test_switch_to_authorization_button_login_page_true(self, driver):
         driver.find_element(*StellarBurgersLocators.BUTTON_LOGIN_PAGE).click()
         assert 'login' in driver.current_url


    # переход на страницу авторизации # по кнопке "Войти" на странице регистрации
    def test_switch_to_authorization_button_from_registration_true(self, driver):
         driver.get(f'{Config.URL}register')
         driver.find_element(*StellarBurgersLocators.LINK_LOGIN_FROM_REGISTRATION).click()
         assert 'login' in driver.current_url


    # переход на страницу авторизации по кнопке "Войти" на странице восстановления пароля
    def test_switch_to_authorization_button_from_password_recovery_true(self, driver):
         driver.get(f'{Config.URL}forgot-password')
         driver.find_element(*StellarBurgersLocators.LINK_LOGIN_FROM_PASSWORD_RECOVERY).click()
         assert 'login' in driver.current_url

