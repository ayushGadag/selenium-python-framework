from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)

    def open_cart(self):
        self.click(self.cart_icon)