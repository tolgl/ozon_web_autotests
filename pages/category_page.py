from locators.category_page_locators import CategoryPageLocators
from pages.base_page import BasePage
import allure


class CategoryPageHelper(BasePage):

    @allure.step('Click first product from category page')
    def click_first_product(self):
        self.find_element(CategoryPageLocators.first_product, wait_time=5).click()
