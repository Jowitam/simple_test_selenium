from TestData.login_data import LoginData as Data
from Locators.LoginPageLocators import LoginPageLocators
from PageObjects.LoginPageObjects import LoginPageObjects
from PageObjects.StartPageObjects import StartPageObject
from TestCaseSetup import TestCaseSetup


class TestLogin(TestCaseSetup):
    """podstawowe testy logowania do platformy allegro"""
    ALLEGRO_URL = "https://allegro.pl.allegrosandbox.pl/"

    def test_correct_messages_when_logging_in_without_login_password(self):
        """test poprawnosci komunikatow po probie logowania bez podania loginu i hasla"""
        self.driver.get(self.ALLEGRO_URL)

        form = StartPageObject(self.driver)
        form.close_rodo(self.driver)

        try:
            form.button_login
        except Exception:
            self.fail("Button not found.")
        form.button_login.click()

        login_page = LoginPageObjects(self.driver)

        try:
            login_page.button_login
        except Exception:
            self.fail("Button not found.")
        login_page.button_login.click()

        self.assertEqual(self.driver.find_element_by_xpath(LoginPageLocators.MESSAGE_wrong_email).text,
                         Data.text_message_email, "Incorrect message in the absence of an email")

        self.assertEqual(self.driver.find_element_by_xpath(LoginPageLocators.MESSAGE_wrong_password).text,
                         Data.text_message_password, "Incorrect message in the absence of a password")
