from pages.login_page import LoginPage

def test_login_valid(driver):
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login("admin", "password123")
    assert "dashboard" in driver.current_url