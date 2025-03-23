from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from config import BASE_URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL

    @allure.step('Open page')
    def go_to_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, wait_time=15):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator))
