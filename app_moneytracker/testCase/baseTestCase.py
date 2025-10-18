import unittest
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options as Options

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        options = Options
        options.platform_name = 'Android'
        options.app_package = 'com.blogspot.e_kanivets.moneytracker'
        options.udid = '354706972253037'
        options.automation_name = 'UiAutomator2'
        options.app_activity = 'com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity'
        options.no_reset = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()

