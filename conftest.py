import pytest
import os

@pytest.fixture(autouse=True)
def setup():
    # Create directory if it does not exist
    os.makedirs('screenshots/test_iphone_cart_workflow', exist_ok=True)

def take_screenshot(driver, name):
    driver.save_screenshot(f"screenshots/test_iphone_cart_workflow/{name}.png")