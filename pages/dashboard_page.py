class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def logout(self):
        self.driver.find_element("id", "logout").click()