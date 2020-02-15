import TestData.login_data as data
from Locators.LoginPageLocators import LoginPageLocators
from PageObjects.LoginPageObjects import LoginPageObjects
from PageObjects.StartPageObjects import StartPageObject
from TestCaseSetup import TestCaseSetup


class TestLogin(TestCaseSetup):
    ALLEGRO_URL = "https://allegro.pl.allegrosandbox.pl/"

    def test_correct_messages_when_logging_in_without_login_password(self):
        self.driver.get(self.ALLEGRO_URL)

        form = StartPageObject(self.driver)
        form.close_rodo(self.driver)

        try:
            form.button_login
        except Exception:
            self.fail("Brak przycisku")
        form.button_login.click()

        login_page = LoginPageObjects(self.driver)

        try:
            login_page.button_login
        except Exception:
            self.fail("Brak przycisku")
        login_page.button_login.click()

        self.assertTrue(self.driver.find_element_by_xpath(LoginPageLocators.MESSAGE_wrong_email).text,
                        data.text_massege_email)

        self.assertTrue(self.driver.find_element_by_xpath(LoginPageLocators.MESSAGE_wrong_password).text,
                        data.text_massege_password)
