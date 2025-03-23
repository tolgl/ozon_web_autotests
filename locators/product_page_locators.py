from selenium.webdriver.common.by import By


class ProductPageLocators:
    button_add_to_cart = (By.XPATH, ".//div[text()='Добавить в корзину']/../..")
    text_passed_button_add_to_cart = (By.XPATH, ".//div[@data-widget='webAddToCart']//span[@class='tsBodyControl500Medium']")
