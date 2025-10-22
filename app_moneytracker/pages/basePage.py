from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator)))
        element.click()

    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):

        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))

            return element.text
        except TimeoutException:
            print(f"Erro: Elemento com localizador '{locator}' não foi encontrado a tempo.")

            return None

    def get_toast_text(self):

        try:
            toast_locator = (AppiumBy.XPATH, '//android.widget.Toast')
            toast_element = self.wait.until(EC.presence_of_element_located(toast_locator))

            return toast_element.get_attribute('name')
        except TimeoutException:
            print(f"Erro: Mensagem Toast não foi encontrada a tempo.")

            return None

