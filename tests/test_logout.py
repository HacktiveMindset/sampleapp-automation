from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_logout(driver):
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login("admin", "password123")

    dashboard = DashboardPage(driver)
    dashboard.logout()
    assert "login" in driver.current_url