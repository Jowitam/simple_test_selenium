from Locators.StartPageLocators import StartPageLocators
import BasicActions

class StartPageObject:
    def __init__(self, driver):
        self.locator = StartPageLocators()
        find = driver.find_element_by_xpath

        self.button_login = find(self.locator.BUTTON_login)

    def close_rodo(self, driver):
        BasicActions.wait_element(driver, self.locator.BUTTON_close_rodo)
        self.button_rodo = driver.find_element_by_xpath(self.locator.BUTTON_close_rodo)
        self.button_rodo.click()

