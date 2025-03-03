from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import selector


class ProductPage:
    def __init__(self,driver):
        self.driver = driver

    def click_first_product(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.product_first_product)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_first_product: element not found')
        except ElementClickInterceptedException:
            print('click_first_product: element not clickable')
        return False
    
    def click_add_to_cart(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.product_detail_button_add_to_cart)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_first_product: element not found')
        except ElementClickInterceptedException:
            print('click_first_product: element not clickable')
        return False