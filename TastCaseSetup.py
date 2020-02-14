import time
import unittest

from selenium import webdriver


class TestCaseSetup(unittest.TestCase):
    """klasa bazowa testow - co dzieje sie przed i po tescie"""

    # def setUpClass(self):
    #     # jedno okno dla wszystkich testow
    #     pass

    def setUp(self):
        # nowe okno dla kazdego testu
        self.driver = self.get_driver()

    def tearDown(self):
        # zamkniecie po kazdym tescie
        filename = "{}{}{}.png".format(time.strftime("%y%m_%d_"), self._testMethodName, time.strftime("_%H_%M_%S"))
        self.driver.save_screenshot(filename)
        self.driver.close()

    # def tearDownClass(self):
    #     # zamkniecie po wszystkich testach
    #     pass

    def get_driver(self):
        args = ['--no-sandbox', '--window-size=1366x768', '--disable-gpu', '--start-maximized',
                '--ignore-certificate-errors', '--disable-extensions', '--disable-notifications']
        options = webdriver.ChromeOptions()
        for arg in args:
            options.add_argument(arg)
        driver = webdriver.Chrome(options=options)
        return driver
