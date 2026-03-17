from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_to_cart(logged_in_user):

    driver = logged_in_user

    product = ProductPage(driver)
    product.add_product_to_cart()
    product.open_cart()

    cart = CartPage(driver)

    assert "Sauce Labs Backpack" in cart.is_product_in_cart()