import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.config import Config
from src.locators import StellarBurgersLocators
from src.data import Data

# фикстура для создания драйвера на Chrome
@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()

# фикстура для главной страницы авторизованного пользователя
@pytest.fixture(scope="class")
def auth_driver():
    driver_noexit = webdriver.Chrome()
    driver_noexit.get(f'{Config.URL}login')
    driver_noexit.find_element(*StellarBurgersLocators.AUTH_EMAIL_FIELD).send_keys(Data.LOGIN)
    driver_noexit.find_element(*StellarBurgersLocators.AUTH_PASSWORD_FIELD).send_keys(Data.PASSWORD)
    driver_noexit.find_element(*StellarBurgersLocators.AUTH_BUTTON).click()
    WebDriverWait(driver_noexit, 3).until(EC.visibility_of_element_located((StellarBurgersLocators.BUTTON_ORDER)))
    yield driver_noexit
    driver_noexit.quit()
