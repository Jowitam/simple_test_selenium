import BasicActions
from Locators.LoginPageLocators import LoginPageLocators


class LoginPageObjects:
    def __init__(self, driver):
        self.locator = LoginPageLocators()
        find = driver.find_element_by_xpath

        BasicActions.wait_element(driver, self.locator.CONTAINER_login)
        self.button_login = find(self.locator.BUTTON_login)
