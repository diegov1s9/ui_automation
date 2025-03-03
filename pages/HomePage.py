from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import selector

class HomePage:
    def __init__(self,driver):
        self.driver = driver
    
    def set_input_search(self, text_to_search):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(selector.homepage_input_search)
            )
            element.clear()
            element.send_keys(text_to_search)
            return element
        except TimeoutException:
            print('set_input_search: element not found')
            return None
        
    def click_in_button_search(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.homepage_button_search)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_in_button_search: element not found')
        except ElementClickInterceptedException:
            print('click_in_button_search: element not clickable')
        return False
    
    def click_in_cart(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.homepage_button_cart)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_in_cart: element not found')
        except ElementClickInterceptedException:
            print('click_in_cart: element not clickable')
        return False
    
    def click_link_view_cart(self):
        try:
            element = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(selector.homepage_link_view_cart)
            )
            element.click()
            return True
        except TimeoutException:
            print('click_link_view_cart: element not found')
        except ElementClickInterceptedException:
            print('click_link_view_cart: element not clickable')
        return False
