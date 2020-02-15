import os
import time
import unittest

from selenium import webdriver


class TestCaseSetup(unittest.TestCase):
    """klasa bazowa testow - co dzieje sie przed i po tescie"""

    def setUp(self):
        # nowe okno dla kazdego testu
        self.driver = self.get_driver()

    def tearDown(self):
        # po kazdym tescie - screenshot oraz zamkniecie przegladarki
        filename = "{}{}{}.png".format(time.strftime("%y%m_%d_"), self._testMethodName, time.strftime("_%H_%M_%S"))
        screenshot_directory = './Screenshots/'

        try:
            os.mkdir(screenshot_directory)
        except FileExistsError:
            pass

        self.driver.save_screenshot(screenshot_directory + filename)
        self.driver.close()

    def get_driver(self):
        # ustawienia przegladarki chrome
        args = ['--no-sandbox', '--window-size=1366x768', '--disable-gpu', '--start-maximized',
                '--ignore-certificate-errors', '--disable-extensions', '--disable-notifications']
        options = webdriver.ChromeOptions()
        for arg in args:
            options.add_argument(arg)
        driver = webdriver.Chrome(options=options)
        return driver
