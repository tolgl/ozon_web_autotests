from pages.base_page import BasePage
from pages.product_page import ProductPageHelper
from pages.header_page import HeaderPageHelper
from pages.catalog_menu_page import CatalogMenuPageHelper
from pages.category_page import CategoryPageHelper
import allure


class TestProductAddCart:

    @allure.title('Test add product to cart from product page')
    def test_product_add_in_cart_from_product_page(self, driver):
        base_page = BasePage(driver)
        base_page.go_to_page()
        header = HeaderPageHelper(driver)
        header.click_button_catalog_menu()
        catalog_menu = CatalogMenuPageHelper(driver)
        catalog_menu.click_first_section_catalog_menu()
        category_page = CategoryPageHelper(driver)
        category_page.click_first_product()
        product_page = ProductPageHelper(driver)
        product_page.click_button_add_to_cart()

        assert product_page.get_text_pressed_button_add_to_cart() == 'В корзине'
