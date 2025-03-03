from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.HomePage import HomePage
import data
from conftest import take_screenshot
from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage

class TestYourStore:
    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("window-size=1920x1080")
        
        service = Service('/usr/bin/chromedriver') 
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)

    def test_iphone_cart_workflow(self):
        # Open web
        self.driver.get(data.base_url)

        # Find a product in home page
        home_page = HomePage(self.driver)
        home_page.set_input_search(data.product_search)
        home_page.click_in_button_search()

        # Select the first option that appears.
        product = ProductPage(self.driver)
        product.click_first_product()
        take_screenshot(self.driver, "click_first_product")

        # add product to cart
        product.click_add_to_cart()

        # Enter the shopping cart button.
        home_page.click_in_cart()
        home_page.click_link_view_cart()

        # Validate product exists in cart 
        shopping = ShoppingCartPage(self.driver)
        assert shopping.validate_product_exists(data.product_search), \
            "validate_product_exists product does not exist"
        take_screenshot(self.driver,'validate_product_exists')

        # Remove first product from the shopping cart.
        shopping.remove_first_product()

        # Validate that the shopping cart is empty
        assert shopping.validate_shopping_cart_is_empty(), \
            "validate_shopping_cart_is_empty element not found"
        take_screenshot(self.driver,'validate_shopping_cart_is_empty')
        
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()