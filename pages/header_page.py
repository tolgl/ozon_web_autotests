from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage
import allure


class HeaderPageHelper(BasePage):

    @allure.step('Click button catalog')
    def click_button_catalog_menu(self):
        self.find_element(HeaderPageLocators.button_catalog_menu, wait_time=5).click()
