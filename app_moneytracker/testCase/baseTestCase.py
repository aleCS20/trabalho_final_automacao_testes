import unittest
import os

from appium import webdriver
from appium.options.android import UiAutomator2Options as Options

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.platform_name = 'Android'
        options.app_package = 'com.blogspot.e_kanivets.moneytracker'
        options.udid = '354706972253037'
        options.automation_name = 'UiAutomator2'
        options.app_activity = 'com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity'
        options.no_reset = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)

        self.evidence_path = os.path.join('app_moneytracker', 'test_evidences', 'screenshots')

        os.makedirs(self.evidence_path, exist_ok=True)

        self.screenshot_counters = {}

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def _take_screenshot(self):
        """Tira um screenshot da tela atual e salva com um nome padronizado.
        Ex: test_cadastrar_conta_sucesso_0.png"""
        method_name = self.id().split('.')[-1]

        counter = self.screenshot_counters.get(method_name, 0)

        file_name = f"{method_name}_{counter}.png"

        full_path = os.path.join(self.evidence_path, file_name)

        self.driver.save_screenshot(full_path)
        self.screenshot_counters[method_name] = counter + 1

        print(f"Evidência capturada: {full_path}")

if __name__ == '__main__':
    unittest.main()

