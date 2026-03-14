from pages.login_page import LoginPage

def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)
    login.login("wrong_user", "wrong_password")

    error_message = driver.find_element("xpath", "//h3[@data-test='error']")
    
    assert error_message.is_displayed()