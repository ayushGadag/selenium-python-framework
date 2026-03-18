from utils.logger import get_logger
from pages.product_page import ProductPage
from pages.cart_page import CartPage

logger = get_logger()

def test_add_to_cart(logged_in_user):

    driver = logged_in_user

    logger.info("Starting add to cart test")

    product = ProductPage(driver)
    product.add_product_to_cart()
    logger.info("Product added to cart")

    product.open_cart()

    cart = CartPage(driver)

    assert "Sauce Labs Backpack" in cart.is_product_in_cart()

    logger.info("Test completed successfully")