from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage
import allure


class ProductPageHelper(BasePage):

    @allure.step('Click button add to cart')
    def click_button_add_to_cart(self):
        self.find_element(ProductPageLocators.button_add_to_cart, wait_time=5).click()

    @allure.step('Click button add to cart')
    def get_text_pressed_button_add_to_cart(self):
        return self.find_element(ProductPageLocators.text_passed_button_add_to_cart, wait_time=5).text
