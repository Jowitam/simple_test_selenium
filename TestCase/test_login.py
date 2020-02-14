from Locators.LoginPageLocators import LoginPageLocators
from PageObjects.LoginPageObjects import LoginPageObjects
from PageObjects.StartPageObjects import StartPageObject
from TastCaseSetup import TestCaseSetup


class TestLogin(TestCaseSetup):
    ALLEGRO_URL = "https://allegro.pl.allegrosandbox.pl/"
    text_massege_email = "Podaj login lub e-mail"

    def test_button_login_exist(self):
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
                        self.text_massege_email)
