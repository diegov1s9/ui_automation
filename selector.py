from selenium.webdriver.common.by import By

homepage_input_search = (By.NAME, 'search')
homepage_button_search = (By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
homepage_button_cart = (By.ID, 'cart-total')
homepage_link_view_cart = (By.XPATH, "//a[contains(.,'View Cart')]")

product_first_product = (By.CSS_SELECTOR, '.product-thumb .image')
product_detail_button_add_to_cart = (By.ID, 'button-cart')

def shopping_search_element(product):
    return (By.XPATH, f'//table[@class="table table-bordered"]//td[contains(@class, "text-left")]//a[text()="{product}"]')

shopping_first_button_remove = (By.CSS_SELECTOR, '.input-group.btn-block .btn.btn-danger')
shopping_text_cart_is_empty = (By.XPATH, "//div[@id='content' and .//p[text()='Your shopping cart is empty!']]")