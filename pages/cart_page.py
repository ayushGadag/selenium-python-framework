from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    cart_item = (By.CLASS_NAME, "inventory_item_name")

    def is_product_in_cart(self):
        return self.get_text(self.cart_item)