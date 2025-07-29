from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get("https://example.com/login")

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login").click()

    def is_login_failed(self):
        return "Invalid credentials" in self.driver.page_source