from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard_title(driver):
    login = LoginPage(driver)
    login.go_to_login_page()
    login.login("admin", "password123")

    dashboard = DashboardPage(driver)
    assert "Dashboard" in dashboard.get_title()