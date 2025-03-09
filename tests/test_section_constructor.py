import pytest

from src.locators import StellarBurgersLocators

@pytest.mark.usefixtures("main_page")
class TestStellarBurgersConstructor:
    # Переход к разделу "Булки"
    def test_switch_to_buns_section_true(self, driver):
        # сначала кликаем на кнопку "Соусы", чтобы кнопка "Булки" стала кликабельной
        driver.find_element(*StellarBurgersLocators.BUTTON_SAUCES).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_BUNS).click()
        assert driver.find_element(*StellarBurgersLocators.CURRENT_BUNS)

    # Переход к разделу "Соусы"
    def test_switch_to_sauces_section_true(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_SAUCES).click()
        assert driver.find_element(*StellarBurgersLocators.CURRENT_SAUCES)

    # Переход к разделу "Начинки"
    def test_switch_to_fillings_section_true(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_FILLINGS).click()
        assert driver.find_element(*StellarBurgersLocators.CURRENT_FILLINGS)

