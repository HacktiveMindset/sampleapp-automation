from pages.login_page import LoginPage

def test_login_invalid(driver):
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login("wrong", "wrongpass")
    assert login.is_login_failed()