from locators.catalog_menu_page_locators import CatalogMenuPageLocators
from pages.base_page import BasePage
import allure


class CatalogMenuPageHelper(BasePage):

    @allure.step('Click first section form catalog menu')
    def click_first_section_catalog_menu(self):
        self.find_element(CatalogMenuPageLocators.first_section, wait_time=5).click()
