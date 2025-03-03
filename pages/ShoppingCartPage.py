from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import selector


class ShoppingCartPage:
    def __init__(self,driver):
        self.driver = driver

    def validate_product_exists(self, product):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(selector.shopping_search_element(product))
            )
            return True
        except TimeoutException:
            return False
        
    def remove_first_product(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.shopping_first_button_remove)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_first_product: element not found')
        except ElementClickInterceptedException:
            print('click_first_product: element not clickable')
        return False

    def validate_shopping_cart_is_empty(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(selector.shopping_text_cart_is_empty)
            )
            return True
        except TimeoutException:
            return False