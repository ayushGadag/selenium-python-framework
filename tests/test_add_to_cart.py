from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By


def test_add_to_cart(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    product = ProductPage(driver)
    product.add_product_to_cart()
    product.open_cart()

    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name")

    assert cart_item.is_displayed()